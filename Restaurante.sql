CREATE DATABASE IF NOT EXISTS foodsoft;

USE foodsoft;		

CREATE TABLE IF NOT EXISTS empleado(
	id_empleado INT NOT NULL,
	nombre VARCHAR(100) NOT NULL,
	cargo VARCHAR(20) NOT NULL,
	contraseña INT NOT NULL,
	status_empleado BOOL NOT NULL,
	PRIMARY KEY(id_empleado)
);

CREATE TABLE IF NOT EXISTS proveedor(
	id_proveedor INT NOT NULL,
	nombre VARCHAR(30) NOT NULL,
	telefono INT(10) NOT NULL,
	correo VARCHAR(80) NOT NULL,
	tipo_cadena VARCHAR(20) NOT NULL,
	rfc VARCHAR(13),
	PRIMARY KEY(id_proveedor)
);

CREATE TABLE IF NOT EXISTS platillo(
	id_platillo INT NOT NULL,
	nombre VARCHAR NOT NULL,
	estado BOOL NOT NULL,
	descripcion VARCHAR(100),
	precio FLOAT NOT NULL,
	PRIMARY KEY(id_platillo)
);

CREATE TABLE IF NOT EXISTS insumo(
	nombre VARCHAR(30) NOT NULL,
	stock_min INT NOT NULL,
	stock_max INT NOT NULL,
	precio FLOAT NOT NULL,
	id_proveedor INT NOT NULL,
	PRIMARY KEY(nombre),
	FOREIGN KEY(id_proveedor) REFERENCES proveedor(id_proveedor) 
);

-- COMPRA DE INSUMOS A PROVEEDOR 
CREATE TABLE IF NOT EXISTS icompra(
	id_icompra INT NOT NULL,
	id_proveedor INT NOT NULL,
	id_empleado INT NOT NULL,
	fecha DATE,
	PRIMARY KEY(id_icompra),
	FOREIGN KEY(id_proveedor) REFERENCES proveedor(id_proveedor),
	FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE IF NOT EXISTS icomprainsumo(
	id_icomprainsumo INT NOT NULL,
	id_icompra INT NOT NULL,
	insumo VARCHAR(30) NOT NULL,
	precio FLOAT NOT NULL,
	cantidad INT NOT NULL,
	PRIMARY KEY(id_icomprainsumo),
	FOREIGN KEY(id_icompra) REFERENCES icompra(id_icompra),
	FOREIGN KEY(insumo) REFERENCES insumo(nombre)
);

-- COMANDA: PEDIDOS
CREATE TABLE IF NOT EXISTS vcomanda(
	id_vcomanda INT NOT NULL,
	id_empleado INT NOT NULL,
	mesa INT NOT NULL,
	PRIMARY KEY(id_vcomand),
	FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE IF NOT EXISTS comanda(
	id_comanda INT NOT NULL,
	id_vcomanda INT NOT NULL,
	id_platillo INT NOT NULL,
	cantidad INT NOT NULL,
	precio FLOAT NOT NULL,
	PRIMARY KEY(id_comanda),
	FOREIGN KEY(id_vcomanda) REFERENCES vcomanda(id_vcomanda),
	FOREIGN KEY(id_platillo) REFERENCES platillo(id_platillo)
);

-- MERMA
CREATE TABLE IF NOT EXISTS tmerma(
	id_tmerma INT NOT NULL,
	id_empleado INT NOT NULL,
	fecha DATE,
	PRIMARY KEY(id_tmerma),
	FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE IF NOT EXISTS merma(
	id_merma INT NOT NULL,
	id_tmerma INT NOT NULL,
	insumo VARCHAR(30) NOT NULL,
	cantidad INT NOT NULL,
	motivo VARCHAR(80) NOT NULL, 
	PRIMARY KEY(id_merma),
	FOREIGN KEY(id_tmerma) REFERENCES tmerma(id_tmerma),
	FOREIGN KEY(insumo) REFERENCES insumo(nombre)
);
