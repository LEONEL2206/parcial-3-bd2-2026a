USE taller_mecanico;

-- =========================
-- CLIENTES (10)
-- =========================

INSERT INTO cliente (nombres, documento, telefono) VALUES
('Juan Perez', '1001', '3001111111'),
('Maria Gomez', '1002', '3002222222'),
('Carlos Ruiz', '1003', '3003333333'),
('Ana Torres', '1004', '3004444444'),
('Luis Martinez', '1005', '3005555555'),
('Laura Diaz', '1006', '3006666666'),
('Pedro Castro', '1007', '3007777777'),
('Sofia Herrera', '1008', '3008888888'),
('Andres Rojas', '1009', '3009999999'),
('Valentina Mora', '1010', '3010000000');

-- =========================
-- VEHICULOS (15)
-- =========================

INSERT INTO vehiculo (placa, modelo, año, id_cliente) VALUES
('ABC101', 'Mazda 3', 2020, 1),
('ABC102', 'Chevrolet Spark', 2018, 1),
('ABC103', 'Toyota Corolla', 2021, 2),
('ABC104', 'Renault Logan', 2019, 2),
('ABC105', 'Kia Rio', 2022, 3),
('ABC106', 'Hyundai Accent', 2017, 4),
('ABC107', 'Nissan Versa', 2020, 5),
('ABC108', 'Mazda CX5', 2021, 6),
('ABC109', 'Toyota Hilux', 2019, 7),
('ABC110', 'Chevrolet Onix', 2022, 8),
('ABC111', 'Renault Duster', 2018, 9),
('ABC112', 'Suzuki Swift', 2020, 10),
('ABC113', 'Kia Sportage', 2021, 3),
('ABC114', 'Mazda 2', 2019, 5),
('ABC115', 'Toyota Yaris', 2023, 7);

-- =========================
-- MECANICOS (5)
-- =========================

INSERT INTO mecanico (nombres, especialidad) VALUES
('Jorge Ramirez', 'Motor'),
('Diego Lopez', 'Suspension'),
('Camilo Vargas', 'Electricidad'),
('Mateo Sanchez', 'Frenos'),
('Daniel Ortiz', 'Transmision');

-- =========================
-- REPUESTOS (30)
-- =========================

INSERT INTO repuesto (nombre, stock, precio) VALUES
('Filtro Aceite', 50, 25000),
('Filtro Aire', 40, 30000),
('Bujia', 100, 12000),
('Pastillas Freno', 30, 85000),
('Disco Freno', 20, 180000),
('Amortiguador', 25, 220000),
('Correa Distribucion', 15, 160000),
('Bateria', 18, 350000),
('Radiador', 10, 420000),
('Alternador', 12, 500000),
('Aceite Motor', 100, 45000),
('Sensor ABS', 10, 120000),
('Bombillo LED', 60, 15000),
('Filtro Combustible', 25, 28000),
('Empaque Culata', 8, 190000),
('Reten Cigüeñal', 15, 45000),
('Kit Embrague', 10, 550000),
('Rodamiento', 40, 35000),
('Terminal Direccion', 20, 70000),
('Bomba Agua', 18, 170000),
('Bomba Gasolina', 12, 260000),
('Tensor Correa', 25, 80000),
('Valvula Escape', 30, 65000),
('Valvula Admision', 30, 65000),
('Manguera Radiador', 20, 40000),
('Liquido Frenos', 60, 18000),
('Liquido Refrigerante', 60, 25000),
('Fusible', 200, 2000),
('Relay', 80, 12000),
('Sensor Temperatura', 15, 95000);

-- =========================
-- ORDENES DE TRABAJO (20)
-- =========================

INSERT INTO orden_trabajo
(id_vehiculo, problema_reportado, fecha_entrada, fecha_salida, estado, costo_total)
VALUES
(1,'Cambio de aceite','2026-04-01','2026-04-01','Finalizada',70000),
(2,'Fallas en frenos','2026-04-02','2026-04-03','Finalizada',250000),
(3,'Problema electrico','2026-04-03','2026-04-04','Finalizada',180000),
(4,'Cambio de bateria','2026-04-04','2026-04-04','Finalizada',400000),
(5,'Revision general','2026-04-05','2026-04-05','Finalizada',120000),
(6,'Cambio amortiguadores','2026-04-06','2026-04-07','Finalizada',500000),
(7,'Cambio correa','2026-04-07','2026-04-08','Finalizada',320000),
(8,'Problema motor','2026-04-08',NULL,'En reparacion',0),
(9,'Falla ABS','2026-04-09',NULL,'Diagnosticado',0),
(10,'Cambio aceite','2026-04-10','2026-04-10','Finalizada',70000),
(11,'Cambio embrague','2026-04-11',NULL,'En reparacion',0),
(12,'Problema refrigeracion','2026-04-12',NULL,'Recibido',0),
(13,'Falla direccion','2026-04-13',NULL,'Recibido',0),
(14,'Cambio frenos','2026-04-14',NULL,'Diagnosticado',0),
(15,'Cambio filtro aire','2026-04-15',NULL,'Recibido',0),
(1,'Revision suspension','2026-04-16',NULL,'Recibido',0),
(3,'Cambio bateria','2026-04-16',NULL,'Recibido',0),
(5,'Falla electrica','2026-04-17',NULL,'Recibido',0),
(7,'Cambio aceite','2026-04-17',NULL,'Recibido',0),
(9,'Revision general','2026-04-18',NULL,'Recibido',0);

-- =========================
-- ASIGNACIONES
-- =========================

INSERT INTO asignacion_mecanico (id_orden,id_mecanico,rol) VALUES
(1,1,'Motor'),
(2,4,'Frenos'),
(3,3,'Electricidad'),
(4,3,'Electricidad'),
(5,1,'Revision'),
(6,2,'Suspension'),
(7,1,'Motor'),
(8,1,'Motor'),
(9,3,'Diagnostico'),
(10,1,'Motor');

-- =========================
-- DETALLE REPUESTOS
-- =========================

INSERT INTO detalle_repuesto
(id_orden,id_repuesto,cantidad,subtotal)
VALUES
(1,1,1,25000),
(1,11,1,45000),
(2,4,1,85000),
(2,5,1,180000),
(3,12,1,120000),
(4,8,1,350000),
(6,6,2,440000),
(7,7,1,160000),
(10,1,1,25000),
(10,11,1,45000);