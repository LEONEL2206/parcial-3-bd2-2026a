CREATE DATABASE taller_mecanico;
USE taller_mecanico;

-- =========================
-- 1. CLIENTE
-- =========================
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    documento VARCHAR(20) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);

-- =========================
-- 2. VEHICULO
-- =========================
CREATE TABLE vehiculo (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10) UNIQUE NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    anio INT,
    id_cliente INT NOT NULL,

    FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
        ON DELETE CASCADE
);

-- =========================
-- 3. MECANICO
-- =========================
CREATE TABLE mecanico (
    id_mecanico INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100)
);

-- =========================
-- 4. ORDEN DE TRABAJO
-- =========================
CREATE TABLE orden_trabajo (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo INT NOT NULL,

    problema_reportado TEXT NOT NULL,

    fecha_entrada DATE NOT NULL,
    fecha_salida DATE NULL,

    estado VARCHAR(30) DEFAULT 'Recibido',

    mano_obra DECIMAL(10,2) DEFAULT 0,
    costo_total DECIMAL(10,2) DEFAULT 0,

    FOREIGN KEY (id_vehiculo)
        REFERENCES vehiculo(id_vehiculo)
        ON DELETE CASCADE
);

-- =========================
-- 5. ASIGNACION MECANICO
-- =========================
CREATE TABLE asignacion_mecanico (
    id_asignacion INT AUTO_INCREMENT PRIMARY KEY,

    id_orden INT NOT NULL,
    id_mecanico INT NOT NULL,

    rol VARCHAR(50),

    FOREIGN KEY (id_orden)
        REFERENCES orden_trabajo(id_orden)
        ON DELETE CASCADE,

    FOREIGN KEY (id_mecanico)
        REFERENCES mecanico(id_mecanico)
        ON DELETE CASCADE
);

-- =========================
-- 6. REPUESTO
-- =========================
CREATE TABLE repuesto (
    id_repuesto INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    stock INT DEFAULT 0,

    precio DECIMAL(10,2) NOT NULL
);

-- =========================
-- 7. DETALLE REPUESTO
-- =========================
CREATE TABLE detalle_repuesto (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,

    id_orden INT NOT NULL,
    id_repuesto INT NOT NULL,

    cantidad INT NOT NULL,

    subtotal DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (id_orden)
        REFERENCES orden_trabajo(id_orden)
        ON DELETE CASCADE,

    FOREIGN KEY (id_repuesto)
        REFERENCES repuesto(id_repuesto)
        ON DELETE CASCADE
);