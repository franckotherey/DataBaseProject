-- /* Creacion de las tablas */
DROP SCHEMA proyecto1k CASCADE;
CREATE SCHEMA IF NOT EXISTS proyecto1k;
SET search_path TO proyecto1k;

CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER, -- pk
    dni VARCHAR(12),
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(50),
    contrasenia VARCHAR(50),
    telefono INTEGER,
    fecha_nacimiento DATE,
    ubicacion_id INTEGER --fk
);

CREATE TABLE IF NOT EXISTS ubicacion (
    id INTEGER, --pk
    pais VARCHAR(50),
    ciudad VARCHAR(50),
    provincia VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS pedido (
    codigo VARCHAR(12), --pk
    costo_envio DOUBLE PRECISION,
    direccion_envio VARCHAR(50),
    impuesto_total DOUBLE PRECISION,
    fecha DATE,
    forma_pago VARCHAR(50),
    monto_total DOUBLE PRECISION,
    fecha_entrega DATE,
    descuento_total DOUBLE PRECISION,
    clienteid INTEGER --fk
);

CREATE TABLE IF NOT EXISTS comentarioProducto (
    id INTEGER, -- pk
    clienteid INTEGER, --fk
    fecha DATE,
    texto VARCHAR(100),
    idioma VARCHAR(25),
    productoid INTEGER --fk
);

CREATE TABLE IF NOT EXISTS producto (
    id INTEGER, --pk
    descripcion VARCHAR(100),
    sku VARCHAR(15),
    marca VARCHAR(50),
    talla VARCHAR(25),
    nombre VARCHAR(50),
    precio DOUBLE PRECISION,
    material VARCHAR(50),
    stock INTEGER,
    imagen VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER, --pk
    tipo VARCHAR(50),
    subtipo VARCHAR(50),
    descripcion VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS proveedor (
    id INTEGER, --pk
    ubicacion VARCHAR(100),
    ruc VARCHAR(50),
    nombre VARCHAR(50),
    email VARCHAR(50),
    telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS responde (
    comentarioProductoid INTEGER, --pk fk
    comentarioProducto2id INTEGER --pk fk
);

CREATE TABLE IF NOT EXISTS perteneceP (
    productoid INTEGER, --pk fk
    categoriaid INTEGER --pk fk
);

CREATE TABLE IF NOT EXISTS proveeP (
    proveedorid INTEGER, --pk fk
    productoid INTEGER --pk fk
);

CREATE TABLE IF NOT EXISTS contieneP (
    pedidocodigo VARCHAR(12), --pk fk
    productoid INTEGER, --pk fk
    descuentoProducto DOUBLE PRECISION,
    cantidad INTEGER,
    subtotal double precision
);

-- /* Restricciones */

-- || Primary Keys || 

-- Cliente
ALTER TABLE cliente ADD CONSTRAINT cliente_pk_id PRIMARY KEY (id);

-- Ubicacion
AlTER TABLE ubicacion ADD CONSTRAINT ubicacion_pk_id PRIMARY KEY (id);

-- Pedido
ALTER TABLE pedido ADD CONSTRAINT pedido_pk_codigo PRIMARY KEY (codigo);

-- ComentarioProducto
ALTER TABLE comentarioProducto ADD CONSTRAINT comentarioProducto_pk_id PRIMARY KEY (id);

-- Producto
ALTER TABLE producto ADD CONSTRAINT producto_pk_id PRIMARY KEY (id);

-- Categoria
ALTER TABLE categoria ADD CONSTRAINT categoria_pk_id  PRIMARY KEY (id);

-- Proveedor
ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk_id PRIMARY KEY (id);

-- Responde
ALTER TABLE responde ADD CONSTRAINT reponde_pk_comentarioProductoid_comentarioProducto2id PRIMARY KEY (comentarioProductoid, comentarioProducto2id);

-- PerteneceP
ALTER TABLE perteneceP ADD CONSTRAINT perteneceP_pk_productoid_categoriaid PRIMARY KEY (productoid,categoriaid);

-- ProveeP
ALTER TABLE proveeP ADD CONSTRAINT proveeP_pk_proveedorid_productoid PRIMARY KEY (proveedorid,productoid);

-- ContieneP
ALTER TABLE contieneP ADD CONSTRAINT contieneP_pk_pedidocodigo_productoid PRIMARY KEY (pedidoCodigo,productoid);

-- || Foreign Keys ||

-- Cliente
ALTER TABLE cliente ADD CONSTRAINT ubicacion_fk_id FOREIGN KEY (ubicacion_id) REFERENCES ubicacion(id);

-- Pedido
ALTER TABLE pedido ADD CONSTRAINT cliente_fk_id FOREIGN KEY (clienteid) REFERENCES cliente(id);

-- ComentarioProducto
ALTER TABLE comentarioProducto ADD CONSTRAINT producto_fk_id FOREIGN KEY (productoid) REFERENCES producto(id);
ALTER TABLE comentarioProducto ADD CONSTRAINT cliente_fk_id FOREIGN KEY (clienteid) REFERENCES cliente(id);

-- Responde
ALTER TABLE responde ADD CONSTRAINT comentarioProducto_fk_id FOREIGN KEY (comentarioProductoid) REFERENCES comentarioProducto(id);
ALTER TABLE responde ADD CONSTRAINT comentarioProducto2_fk_id FOREIGN KEY (comentarioProducto2id) REFERENCES comentarioProducto(id);

-- PerteneceP
ALTER TABLE pertenecep ADD CONSTRAINT producto_fk_id FOREIGN KEY (productoid) REFERENCES producto(id);
ALTER TABLE pertenecep ADD CONSTRAINT categoria_fk_id FOREIGN KEY (categoriaid) REFERENCES categoria(id);

-- ProveeP
ALTER TABLE proveep ADD CONSTRAINT proveedor_fk_id FOREIGN KEY (proveedorid) REFERENCES proveedor(id);
ALTER TABLE proveep ADD CONSTRAINT producto_fk_id FOREIGN KEY (productoid) REFERENCES producto(id);

-- ContieneP
ALTER TABLE contienep ADD CONSTRAINT pedido_fk_codigo FOREIGN KEY (pedidocodigo) REFERENCES pedido(codigo);
ALTER TABLE contienep ADD CONSTRAINT producto_fk_id FOREIGN KEY (productoid) REFERENCES producto(id);

--================================================================================================================================

-- || Otras restricciones ||

-- Restriccion: Not Null

ALTER TABLE cliente ALTER COLUMN dni SET NOT NULL;
ALTER TABLE cliente ALTER COLUMN nombre SET NOT NULL;
ALTER TABLE cliente ALTER COLUMN apellido SET NOT NULL;

ALTER TABLE pedido ALTER COLUMN fecha_entrega SET NOT NULL ;
ALTER TABLE pedido ALTER COLUMN forma_pago SET NOT NULL ;
ALTER TABLE pedido ALTER COLUMN monto_total SET NOT NULl;
ALTER TABLE pedido ALTER COLUMN fecha SET NOT NULL;

ALTER TABLE comentarioProducto ALTER COLUMN fecha SET NOT NULL;

ALTER TABLE producto ALTER COLUMN sku SET NOT NULL;
ALTER TABLE producto ALTER COLUMN marca SET NOT NULL;
ALTER TABLE producto ALTER COLUMN nombre SET NOT NULL;
ALTER TABLE producto ALTER COLUMN precio SET NOT NULL;
ALTER TABLE producto ALTER COLUMN stock SET NOT NULL;

AlTER TABLE proveedor ALTER COLUMN ruc SET NOT NULL;
AlTER TABLE proveedor ALTER COLUMN nombre SET NOT NULL;
AlTER TABLE proveedor ALTER COLUMN email SET NOT NULL;

AlTER TABLE categoria ALTER COLUMN tipo SET NOT NULL;
AlTER TABLE contieneP ALTER COLUMN cantidad SET NOT NULL;
AlTER TABLE contieneP ALTER COLUMN subtotal SET NOT NULL;

-- Restriccion: Unique

ALTER TABLE cliente ADD CONSTRAINT cliente_unique_email UNIQUE (email);
ALTER TABLE cliente ADD CONSTRAINT cliente_unique_dni UNIQUE (dni);

AlTER TABLE producto ADD CONSTRAINT producto_unique_sku UNIQUE (sku);

AlTER TABLE proveedor ADD CONSTRAINT proveedor_unique_ruc UNIQUE (ruc);
AlTER TABLE proveedor ADD CONSTRAINT proveedor_unique_email UNIQUE (email);

-- Restriccion: Check

ALTER TABLE contieneP ADD CONSTRAINT contieneP_check_cantidad CHECK (cantidad > 0);
ALTER TABLE contieneP ADD CONSTRAINT contieneP_check_subtotal CHECK (subtotal > 0);

ALTER TABLE pedido ADD CONSTRAINT pedido_check_fechaentrega_fecha CHECK (fecha_entrega >= fecha);

ALTER TABLE producto ADD CONSTRAINT producto_check_stock CHECK (stock >= 0);
ALTER TABLE producto ADD CONSTRAINT producto_check_precio CHECK (precio > 0);
