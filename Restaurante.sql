CREATE DATABASE IF NOT EXISTS restaurante;

USE restaurante;		

CREATE TABLE IF NOT EXISTS empleado(
	id_empleado INT NOT NULL,
	nombre VARCHAR(100) NOT NULL,
	cargo CHAR(20) NOT NULL,
	KEY PRIMARY(id_empleado)
);empleado