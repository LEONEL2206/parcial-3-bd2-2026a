from flask import Flask, render_template, request, redirect
from conexion import conectar

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

# ELIMINAR VEHICULO
@app.route("/eliminar_vehiculo/<int:id>")
def eliminar_vehiculo(id):

    con = conectar()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM vehiculo WHERE id_vehiculo=%s",
        (id,)
    )

    con.commit()

    cur.close()
    con.close()

    return redirect("/vehiculos")


# EDITAR VEHICULO
@app.route("/editar_vehiculo/<int:id>", methods=["GET", "POST"])
def editar_vehiculo(id):

    con = conectar()
    cur = con.cursor()

    if request.method == "POST":

        placa = request.form["placa"]
        modelo = request.form["modelo"]
        anio = request.form["anio"]
        cliente = request.form["cliente"]

        cur.execute("""
            UPDATE vehiculo
            SET placa=%s,
                modelo=%s,
                anio=%s,
                id_cliente=%s
            WHERE id_vehiculo=%s
        """, (placa, modelo, anio, cliente, id))

        con.commit()

        cur.close()
        con.close()

        return redirect("/vehiculos")

    cur.execute(
        "SELECT * FROM vehiculo WHERE id_vehiculo=%s",
        (id,)
    )

    vehiculo = cur.fetchone()

    cur.close()
    con.close()

    return render_template(
        "editar_vehiculo.html",
        vehiculo=vehiculo
    )


# VEHICULOS
@app.route("/vehiculos", methods=["GET", "POST"])
def vehiculos():

    con = conectar()
    cur = con.cursor()

    if request.method == "POST":

        placa = request.form["placa"]
        modelo = request.form["modelo"]
        anio = request.form["anio"]
        cliente = request.form["cliente"]

        cur.execute("""
            INSERT INTO vehiculo
            (placa, modelo, anio, id_cliente)
            VALUES (%s,%s,%s,%s)
        """, (placa, modelo, anio, cliente))

        con.commit()

    cur.execute("SELECT * FROM vehiculo")
    vehiculos = cur.fetchall()

    cur.execute("SELECT * FROM cliente")
    clientes = cur.fetchall()

    cur.close()
    con.close()

    return render_template(
        "vehiculos.html",
        vehiculos=vehiculos,
        clientes=clientes
    )
    
# ELIMINAR CLIENTE
@app.route("/eliminar_cliente/<int:id>")
def eliminar_cliente(id):

    con = conectar()
    cur = con.cursor()

    cur.execute(
        "DELETE FROM cliente WHERE id_cliente=%s",
        (id,)
    )

    con.commit()

    cur.close()
    con.close()

    return redirect("/clientes")


# EDITAR CLIENTE
@app.route("/editar_cliente/<int:id>", methods=["GET","POST"])
def editar_cliente(id):

    con = conectar()
    cur = con.cursor()

    if request.method == "POST":

        nombres = request.form["nombres"]
        documento = request.form["documento"]
        telefono = request.form["telefono"]

        cur.execute("""
            UPDATE cliente
            SET nombres=%s,
                documento=%s,
                telefono=%s
            WHERE id_cliente=%s
        """,
        (nombres, documento, telefono, id))

        con.commit()

        cur.close()
        con.close()

        return redirect("/clientes")

    cur.execute(
        "SELECT * FROM cliente WHERE id_cliente=%s",
        (id,)
    )

    cliente = cur.fetchone()

    cur.close()
    con.close()

    return render_template(
        "editar_cliente.html",
        cliente=cliente
    )

# CLIENTES
@app.route("/clientes", methods=["GET", "POST"])
def clientes():

    con = conectar()
    cur = con.cursor()

    if request.method == "POST":
        nombres = request.form["nombres"]
        documento = request.form["documento"]
        telefono = request.form["telefono"]

        cur.execute("""
            INSERT INTO cliente(nombres, documento, telefono)
            VALUES (%s,%s,%s)
        """, (nombres, documento, telefono))

        con.commit()

    cur.execute("SELECT * FROM cliente")
    datos = cur.fetchall()

    cur.close()
    con.close()

    return render_template("clientes.html", clientes=datos)

# MECANICOS
@app.route("/mecanicos", methods=["GET", "POST"])
def mecanicos():

    con = conectar()
    cur = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        especialidad = request.form["especialidad"]

        cur.execute("""
            INSERT INTO mecanico(nombres, especialidad)
            VALUES (%s,%s)
        """, (nombre, especialidad))

        con.commit()

    cur.execute("SELECT * FROM mecanico")
    datos = cur.fetchall()

    cur.close()
    con.close()

    return render_template("mecanicos.html", mecanicos=datos)

# REPUESTOS
@app.route("/repuestos", methods=["GET", "POST"])
def repuestos():

    con = conectar()
    cur = con.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        stock = request.form["stock"]
        precio = request.form["precio"]

        cur.execute("""
            INSERT INTO repuesto(nombre, stock, precio)
            VALUES (%s,%s,%s)
        """, (nombre, stock, precio))

        con.commit()

    cur.execute("SELECT * FROM repuesto")
    datos = cur.fetchall()

    cur.close()
    con.close()

    return render_template("repuestos.html", repuestos=datos)

# ORDENES
@app.route("/ordenes", methods=["GET", "POST"])
def ordenes():

    con = conectar()
    cur = con.cursor()

    if request.method == "POST":

        vehiculo = request.form["vehiculo"]
        problema = request.form["problema"]
        fecha = request.form["fecha"]

        cur.execute("""
            INSERT INTO orden_trabajo
            (id_vehiculo, problema_reportado, fecha_entrada)
            VALUES (%s,%s,%s)
        """, (vehiculo, problema, fecha))

        con.commit()

    cur.execute("SELECT * FROM orden_trabajo")
    datos = cur.fetchall()

    cur.close()
    con.close()

    return render_template("ordenes.html", ordenes=datos)

if __name__ == "__main__":
    app.run(debug=True)