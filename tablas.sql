-- Creacion de las tablas

CREATE TABLE IF NOT EXISTS cliente(
    id int,
    dni varchar(12),
    nombres varchar(50),
    apellidos varchar(50),
    email varchar(50),
    contrasenia varchar(50),
    telefono int,
    edad int,
    direccionid int
);

CREATE TABLE IF NOT EXISTS direccion(
    id int,
    pais varchar(50),
    ciudad varchar(50),
    provincia varchar(50)
);

CREATE TABLE IF NOT EXISTS pedido(
    codigo varchar(12),
    costoenvio double precision,
    direccionenvio varchar(50),
    impuestototal double precision,
    fecha date,
    formapago varchar(50),
    montototal double precision,
    fechaentrega date,
    descuentototal double precision,
    clienteid int
);

CREATE TABLE IF NOT EXISTS  comentarioProducto(
    id int,
    fecha date,
    texto varchar(100),
    idioma varchar(25),
    productoid int
);

CREATE TABLE IF NOT EXISTS producto(
    id int,
    descripcion varchar(100),
    sku bigint,
    talla varchar(25),
    nombre varchar(50),
    precio double precision,
    material varchar(100),
    stock bigint,
    marca varchar(50),
    imagen varchar(50)
);

CREATE TABLE IF NOT EXISTS categoria(
    id int,
    tipo varchar(50),
    subtipo varchar(50),
    descripcion varchar(100)
);

CREATE TABLE IF NOT EXISTS proveedor(
    id int,
    direccion varchar(100),
    ruc varchar(50),
    nombre varchar(50),
    email varchar(50),
    telefono varchar(20)
);

CREATE TABLE IF NOT EXISTS responde(
    comentarioProductoid int,
    ComentarioProducto2id int
);

CREATE TABLE IF NOT EXISTS perteneceP(
    productoid int,
    categoriaid int
);

CREATE TABLE IF NOT EXISTS proveeP(
    proveedorid int,
    productoid int
);

CREATE TABLE IF NOT EXISTS contieneP(
    pedidoCodigo varchar(12),
    productoid int,
    descuentoProducto double precision,
    cantidad int,
    subtotal double precision
);

-- Restrincciones

-- Primary keys
ALTER TABLE cliente ADD CONSTRAINT pk_cliente PRIMARY KEY  (id);

AlTER TABLE direccion ADD CONSTRAINT pk_direccion PRIMARY KEY (id);

ALTER TABLE pedido ADD CONSTRAINT pk_pedido PRIMARY KEY (codigo);

ALTER TABLE comentarioProducto ADD CONSTRAINT  pk_comentarioProducto PRIMARY KEY (id);

ALTER TABLE producto ADD CONSTRAINT  pk_producto PRIMARY KEY (id);

ALTER TABLE categoria ADD CONSTRAINT  pk_catrgoria  PRIMARY KEY (id);

ALTER TABLE proveedor ADD CONSTRAINT pk_proveedor PRIMARY KEY (id);

ALTER TABLE responde ADD CONSTRAINT pk_respondCP_pk_respondCP2 PRIMARY KEY (comentarioProductoid, ComentarioProducto2id);

ALTER TABLE perteneceP ADD CONSTRAINT  pk_Pid_pk_Cid PRIMARY KEY (productoid,categoriaid);

ALTER TABLE proveep ADD CONSTRAINT pk_ProveedorID_pk_ProductoID PRIMARY KEY (proveedorid,productoid);

ALTER TABLE contieneP ADD CONSTRAINT pk_PedidoCodigo_pk_ProductoId PRIMARY KEY (pedidoCodigo,productoid);

-- Foreing key

ALTER TABLE cliente ADD CONSTRAINT fk_direccionid FOREIGN KEY (direccionid) REFERENCES direccion(id);

ALTER TABLE pedido ADD CONSTRAINT fk_clienteId FOREIGN KEY (clienteid) REFERENCES cliente(id);

ALTER TABLE comentarioProducto ADD CONSTRAINT fk_ProductoId FOREIGN KEY (productoid) REFERENCES producto(id);

ALTER TABLE responde ADD CONSTRAINT fk_comentarioproductoid FOREIGN KEY (comentarioproductoid) REFERENCES comentarioProducto(id);
ALTER TABLE responde ADD CONSTRAINT fk_ComentarioProducto2id FOREIGN KEY (ComentarioProducto2id) REFERENCES comentarioProducto(id);
-- Eliminar foreinkey
-- ALTER TABLE responde DROP CONSTRAINT fk_comentarioproductoid;
-- ALTER TABLE responde DROP CONSTRAINT fk_comentarioproducto2id;
ALTER TABLE pertenecep ADD CONSTRAINT fk_productoId FOREIGN KEY (productoid) REFERENCES producto(id);
ALTER TABLE pertenecep ADD CONSTRAINT fk_CategoriaId FOREIGN KEY (categoriaid) REFERENCES categoria(id);

ALTER TABLE proveep ADD CONSTRAINT fk_proveedorId FOREIGN KEY (proveedorid) REFERENCES proveedor(id);
ALTER TABLE proveep ADD CONSTRAINT fk_productoId FOREIGN KEY (productoid) REFERENCES producto(id);

ALTER TABLE contienep ADD CONSTRAINT fk_PedidoCodigo FOREIGN KEY (pedidocodigo) REFERENCES pedido(codigo);
ALTER TABLE contienep ADD CONSTRAINT fk_ProductoId FOREIGN KEY (productoid) REFERENCES producto(id);
