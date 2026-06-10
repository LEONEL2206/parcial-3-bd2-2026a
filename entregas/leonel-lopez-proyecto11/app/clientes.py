from conexion import conectar

def registrar_cliente():
    nombres = input("Nombre: ")
    documento = input("Documento: ")
    telefono = input("Telefono: ")

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO cliente(nombres, documento, telefono)
        VALUES (%s,%s,%s)
    """, (nombres, documento, telefono))

    con.commit()

    print("Cliente registrado")

    cur.close()
    con.close()