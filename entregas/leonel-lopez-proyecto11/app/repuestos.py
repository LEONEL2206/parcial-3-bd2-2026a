from conexion import conectar

def registrar_repuesto():

    nombre = input("Nombre: ")
    stock = input("Stock: ")
    precio = input("Precio: ")

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO repuesto
        (nombre, stock, precio)
        VALUES (%s,%s,%s)
    """, (nombre, stock, precio))

    con.commit()

    print("Repuesto registrado")

    cur.close()
    con.close()