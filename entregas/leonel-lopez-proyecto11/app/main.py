from clientes import registrar_cliente
from vehiculos import registrar_vehiculo
from mecanicos import registrar_mecanico
from repuestos import registrar_repuesto

from ordenes import (
    crear_orden,
    asignar_mecanico,
    agregar_repuesto,
    cerrar_orden,
    historial
)

while True:

    print("\n===== TALLER MECANICO =====")
    print("1. Registrar Cliente")
    print("2. Registrar Vehiculo")
    print("3. Registrar Mecanico")
    print("4. Registrar Repuesto")
    print("5. Crear Orden")
    print("6. Asignar Mecanico")
    print("7. Agregar Repuesto a Orden")
    print("8. Cerrar Orden")
    print("9. Historial Vehiculo")
    print("0. Salir")

    op = input("Opcion: ")

    if op == "1":
        registrar_cliente()

    elif op == "2":
        registrar_vehiculo()

    elif op == "3":
        registrar_mecanico()

    elif op == "4":
        registrar_repuesto()

    elif op == "5":
        crear_orden()

    elif op == "6":
        asignar_mecanico()

    elif op == "7":
        agregar_repuesto()

    elif op == "8":
        cerrar_orden()

    elif op == "9":
        historial()

    elif op == "0":
        break

    else:
        print("Opcion invalida")