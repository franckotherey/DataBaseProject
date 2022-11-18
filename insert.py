import psycopg2
import random as rd
import names
import datetime 
import radar
from faker import Faker
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
faker = Faker()

#-----------------------------------------------------------------------
def insert_into_table_cliente(n):
    ids = rd.sample([x for x in range(100000, 999999)], 1000)
    dnis = rd.sample([x for x in range(10000000, 99999999)], 1000)
    cursor.execute("SELECT id FROM ubicacion;")
    ids_ubicacion = cursor.fetchall()
    i = 0
    while (i < n):
        try:
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

#-----------------------------------------------
def insert_into_table_pedido(n):
    cursor.execute("SELECT id FROM cliente;")
    ids_cliente = cursor.fetchall()
    codigos = rd.sample([x for x in range(10000000, 99999999)], 1000)
    i = 0
    while (i < n):
        try:
            codigo = str(codigos[i])
            costo_envio = float(0)
            direccion_envio = ' '.join([x.replace('\n', ' ') for x in faker.address().split(' ')])
            impuesto_total = float(0)            
            fecha = str(radar.random_datetime(start = datetime.date(year=2019, month=5, day=24), stop = datetime.date(year=2022, month=11, day=18)))
            forma_pago = rd.choice(['Yape', 'Plin', 'Visa', 'MasterCard', 'Efectivo', 'PayPal', 'Payoneer'])
            monto_total = float(0) 
            # crear un tigger que calcule la suma de todos los subtotales de cada producto que pertenezca a un pedido
            fecha_entrega = str(radar.random_datetime(start = datetime.date.fromisoformat(fecha), stop = datetime.date(year=2022, month=11, day=28)))
            descuento_total = float(0)
            clienteid = int(rd.choice(ids_cliente)[0]) 
            cursor.execute(f"INSERT INTO pedido (codigo, costo_envio, direccion_envio, impuesto_total, fecha, forma_pago, monto_total, fecha_entrega, descuento_total, clienteid) VALUES ('{codigo}', {costo_envio}, '{direccion_envio}', {impuesto_total}, '{fecha}', '{forma_pago}', {monto_total}, '{fecha_entrega}', {descuento_total}, {clienteid});")
            i += 1
        except Exception as e:
            print(e, i)

def update_table_pedido():
    # antes de actualizar la tabla pedido, se tiene que insetar las tuplas en la tabla contieneP
    # el triggers actualiza el monto total
    cursor.execute("SELECT codigo FROM pedido;")
    codigos_pedido = cursor.fetchall()
    i = 0
    while (i < len(codigos_pedido)):
        try:
            cursor.execute(f"SELECT monto_total FROM pedido WHERE codigo = {codigos_pedido[i]};")
            monto_total = float(cursor.fetchone())
            if (monto_total > 0):
                # crear un tigger que calcule eso - la suma de todos los costos* cantidad de cada producto y descuente el monto total
                costo_envio = monto_total * rd.uniform(0.05, 0.2)
                impuesto_total = monto_total * rd.uniform(0.1, 0.2)           
                descuento_total = rd.uniform(monto_total * 0.1, monto_total * 0.3)
                monto_total = monto_total + costo_envio + impuesto_total - descuento_total
                cursor.execute(f"UPDATE pedido SET monto_total = {monto_total}, costo_envio = {costo_envio}, impuesto_total = {impuesto_total}, descuento_total = {descuento_total} WHERE codigo = '{codigos_pedido[i]}';")
            else:
                cursor.execute(f"DELETE FROM pedido WHERE codigo ='{codigos_pedido[i]}';")
            i += 1
        except Exception as e:
            print(e, i)

insert_into_table_pedido(1000)