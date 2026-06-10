from conexion import conectar

def registrar_mecanico():

    nombre = input("Nombre: ")
    especialidad = input("Especialidad: ")

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO mecanico
        (nombres, especialidad)
        VALUES (%s,%s)
    """, (nombre, especialidad))

    con.commit()

    print("Mecanico registrado")

    cur.close()
    con.close()