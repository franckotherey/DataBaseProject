import psycopg2
import random as rd
import names
import datetime
from functions import *

conn = psycopg2.connect (
    database = "bd_group1_3",
    user = "usr_group1_3",
    password = "pass_group1_3",
    host = "194.163.147.223",
    port = "5432",
    options = "-c search_path=proyecto1k"
)

cursor = conn.cursor()
conn.autocommit = True

ids = rd.sample([x for x in range(100000, 999999)], 1000)
dnis = rd.sample([x for x in range(10000000, 99999999)], 1000)

def insert_into_table_cliente(n):
    i = 0
    while (i < n):
        try:
            cursor.execute("SELECT id FROM ubicacion;")
            ids_ubicacion = cursor.fetchall()

            id = ids[i]
            dni = str(dnis[i])
            nombre = names.get_first_name()
            apellido = names.get_last_name()
            email = (nombre[:3] + get_random_string(rd.randint(2,3))+ "." + apellido[:3] + get_random_string(rd.randint(2,3)) + "@gmail.com").lower()
            contrasenia = get_random_string(rd.randint(10, 15))
            telefono = rd.randint(100000000, 999999999)        
            fecha_nacimiento = str(datetime.date(rd.randint(1982,2004), rd.randint(1,12), rd.randint(1,28)))
            ubicacion_id = int(rd.choice(ids_ubicacion)[0]) 
            cursor.execute(f"INSERT INTO cliente (id, dni, nombre, apellido, email, contrasenia, telefono, fecha_nacimiento, ubicacion_id) VALUES ({id}, '{dni}', '{nombre}', '{apellido}', '{email}', '{contrasenia}', {telefono}, '{fecha_nacimiento}', {ubicacion_id});")
            i += 1
        except Exception as e:
            print(e, i)

def insert_into_table_pedido(n):
    i = 0
    while (i < n):
        try:
            cursor.execute("SELECT id FROM cliente;")
            ids_cliente = cursor.fetchall()
            codigo =  



        except Exception as e:
            print(e, i)


#insert_in_table_cliente(1000)

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