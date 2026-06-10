# Notas de Normalización – Proyecto 11: Taller Mecánico

## Descripción General

La base de datos fue diseñada para gestionar clientes, vehículos, órdenes de trabajo, mecánicos y repuestos de un taller mecánico.

El modelo fue normalizado hasta la Tercera Forma Normal (3FN) con el objetivo de evitar redundancia de datos, mejorar la integridad de la información y facilitar el mantenimiento de la base de datos.

---

# Primera Forma Normal (1FN)

Una relación cumple la 1FN cuando:

* Todos los atributos contienen valores atómicos.
* No existen grupos repetitivos.
* Cada fila es única.

Aplicación en el proyecto:

* Cada cliente se almacena una sola vez.
* Cada vehículo tiene una única placa.
* Cada orden de trabajo tiene un identificador único.
* Los repuestos utilizados en una orden se almacenan en una tabla independiente.

Ejemplo:

En lugar de guardar varios repuestos dentro de una misma orden:

Incorrecto:

| Orden | Repuestos               |
| ----- | ----------------------- |
| 1     | Filtro, Aceite, Batería |

Se creó la tabla:

DETALLE_REPUESTO

que permite almacenar cada repuesto en registros independientes.

---

# Segunda Forma Normal (2FN)

Una relación cumple la 2FN cuando:

* Está en 1FN.
* Todos los atributos dependen completamente de la clave primaria.

Aplicación en el proyecto:

La información de los clientes se encuentra únicamente en la tabla CLIENTE.

Los datos del vehículo se almacenan únicamente en VEHICULO.

Los datos de los mecánicos se almacenan únicamente en MECANICO.

No se repiten nombres, teléfonos ni especialidades en otras tablas.

Ejemplo:

La tabla ORDEN_TRABAJO almacena únicamente información relacionada con la orden.

No guarda:

* Nombre del cliente.
* Teléfono del cliente.
* Nombre del mecánico.

Estos datos se obtienen mediante relaciones.

---

# Tercera Forma Normal (3FN)

Una relación cumple la 3FN cuando:

* Está en 2FN.
* No existen dependencias transitivas.

Aplicación en el proyecto:

Las relaciones muchos a muchos fueron separadas mediante tablas intermedias:

## Orden de Trabajo ↔ Mecánico

Se creó la tabla:

ASIGNACION_MECANICO

para almacenar:

* id_orden
* id_mecanico
* rol

Esto evita duplicar información de mecánicos dentro de las órdenes.

---

## Orden de Trabajo ↔ Repuesto

Se creó la tabla:

DETALLE_REPUESTO

para almacenar:

* id_orden
* id_repuesto
* cantidad
* subtotal

Esto evita repetir información de los repuestos dentro de la tabla ORDEN_TRABAJO.

---

# Relaciones del Modelo

CLIENTE (1) ------ (N) VEHICULO

VEHICULO (1) ------ (N) ORDEN_TRABAJO

ORDEN_TRABAJO (1) ------ (N) ASIGNACION_MECANICO

MECANICO (1) ------ (N) ASIGNACION_MECANICO

ORDEN_TRABAJO (1) ------ (N) DETALLE_REPUESTO

REPUESTO (1) ------ (N) DETALLE_REPUESTO

---

# Conclusión

El modelo propuesto cumple con la Primera, Segunda y Tercera Forma Normal (3FN).

La estructura elimina redundancias, evita inconsistencias y permite administrar eficientemente la información de clientes, vehículos, mecánicos, órdenes de trabajo y repuestos dentro del taller mecánico.
