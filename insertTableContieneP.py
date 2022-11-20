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

#---------------------------------------------------------------

def insert_into_table_contieneP(n):
    cursor.execute("SELECT id FROM producto;")
    producto_id = cursor.fetchall()
    cursor.execute("SELECT codigo FROM pedido;")
    codigo_pedido = cursor.fetchall()
    #cursor.execute("SELECT precio FROM producto;")
    #precioProd = cursor.fetchall()
    i = 0
    while(i < n):
        try:
            # subtotal = precio * cantidad
            # descuento producto = 5 - 10
            # cantidad 0 - 20.
            pedidocodigo = rd.choice(codigo_pedido)[0] # fk and pk
            productoid = (rd.choice(producto_id)[0]) # fk and pk
            
            precio_producto_by_id = cursor.execute(f"SELECT precio FROM producto WHERE id ={productoid}"); 
            descuentoproducto = float(rd.randint(2,10))/100 * float(precio_producto_by_id)

            cantidad = rd.randint(1, 40);
            subtotal = (float(precio_producto_by_id) - descuentoproducto) * cantidad

            cursor.execute(f"INSERT INTO contienep(productoid, pedidocodigo, subtotal, cantidad, descuentoproducto) VALUES({productoid}, '{pedidocodigo}', {subtotal}, {cantidad}, {descuentoproducto});")
            i += 1;

        except Exception as e:
            print(e, i)

insert_into_table_contieneP(1000)