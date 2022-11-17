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
    pedidoCodigo int,
    productoid int,
    descuentoProducto double precision,
    cantidad int,
    subtotal double precision
);
