from conexion import conectar

def registrar_vehiculo():

    placa = input("Placa: ")
    modelo = input("Modelo: ")
    anio = input("Año: ")
    cliente = input("ID Cliente: ")

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO vehiculo
        (placa, modelo, año, id_cliente)
        VALUES (%s,%s,%s,%s)
    """, (placa, modelo, anio, cliente))

    con.commit()

    print("Vehiculo registrado")

    cur.close()
    con.close()