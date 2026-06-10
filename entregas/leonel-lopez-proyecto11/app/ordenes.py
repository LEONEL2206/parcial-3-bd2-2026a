from conexion import conectar

def crear_orden():

    vehiculo = input("ID Vehiculo: ")
    problema = input("Problema: ")
    fecha = input("Fecha entrada (YYYY-MM-DD): ")

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO orden_trabajo
        (id_vehiculo, problema_reportado, fecha_entrada)
        VALUES (%s,%s,%s)
    """, (vehiculo, problema, fecha))

    con.commit()

    print("Orden creada")

    cur.close()
    con.close()


def asignar_mecanico():

    orden = input("ID Orden: ")
    mecanico = input("ID Mecanico: ")
    rol = input("Rol: ")

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO asignacion_mecanico
        (id_orden,id_mecanico,rol)
        VALUES (%s,%s,%s)
    """, (orden, mecanico, rol))

    con.commit()

    print("Mecanico asignado")

    cur.close()
    con.close()


def agregar_repuesto():

    orden = input("ID Orden: ")
    repuesto = input("ID Repuesto: ")
    cantidad = int(input("Cantidad: "))

    con = conectar()
    cur = con.cursor()

    cur.execute(
        "SELECT precio, stock FROM repuesto WHERE id_repuesto=%s",
        (repuesto,)
    )

    dato = cur.fetchone()

    if dato is None:
        print("Repuesto no existe")
        return

    precio, stock = dato

    if stock < cantidad:
        print("Stock insuficiente")
        return

    subtotal = precio * cantidad

    cur.execute("""
        INSERT INTO detalle_repuesto
        (id_orden,id_repuesto,cantidad,subtotal)
        VALUES (%s,%s,%s,%s)
    """, (orden, repuesto, cantidad, subtotal))

    cur.execute("""
        UPDATE repuesto
        SET stock = stock - %s
        WHERE id_repuesto=%s
    """, (cantidad, repuesto))

    con.commit()

    print("Repuesto agregado")

    cur.close()
    con.close()


def cerrar_orden():

    orden = input("ID Orden: ")
    fecha = input("Fecha salida: ")
    mano_obra = float(input("Costo mano de obra: "))

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        SELECT IFNULL(SUM(subtotal),0)
        FROM detalle_repuesto
        WHERE id_orden=%s
    """, (orden,))

    repuestos = cur.fetchone()[0]

    total = repuestos + mano_obra

    cur.execute("""
        UPDATE orden_trabajo
        SET fecha_salida=%s,
            estado='Finalizada',
            costo_total=%s
        WHERE id_orden=%s
    """, (fecha, total, orden))

    con.commit()

    print("Total orden:", total)

    cur.close()
    con.close()


def historial():

    placa = input("Placa: ")

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        SELECT o.id_orden,
               o.problema_reportado,
               o.fecha_entrada,
               o.fecha_salida,
               o.estado,
               o.costo_total
        FROM orden_trabajo o
        JOIN vehiculo v
        ON o.id_vehiculo=v.id_vehiculo
        WHERE v.placa=%s
    """, (placa,))

    datos = cur.fetchall()

    for fila in datos:
        print(fila)

    cur.close()
    con.close()