def insert_into_table_pedido(n):
    i = 0
    while (i < n):
        try:
            cursor.execute("SELECT id FROM cliente;")
            ids_cliente = cursor.fetchall()

        except Exception as e:
            print(e, i)

    




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