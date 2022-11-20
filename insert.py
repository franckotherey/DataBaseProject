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
    emails = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com"]
    i = 0
    while (i < n):
        try:
            id = ids[i]
            dni = str(dnis[i])
            nombre = names.get_first_name()
            apellido = names.get_last_name()
            email = (nombre[:3]).lower() + get_random_string(rd.randint(2,3))+ "." + apellido[:3].lower() + get_random_string(rd.randint(2,3)) + rd.choice(emails)
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
    cursor.execute(f"SELECT pedidocodigo, SUM(subtotal) FROM contienep GROUP BY pedidocodigo;")
    lista = cursor.fetchall()
    i = 0
    
    while (i < len(lista)):
        try:
            #codigos_p = codigos_pedido[i][0]
            #cursor.execute(f"SELECT monto_total FROM pedido WHERE codigo='{codigos_p}';")
            pedidocodigo = lista[i][0]
            monto_total = lista[i][1]
            #print(lista)
            #print(monto_total)
            #if (monto_total == 0):
                # crear un tigger que calcule eso - la suma de todos los costos* cantidad de cada producto y descuente el monto total
            costo_envio = round(monto_total * rd.uniform(0.05, 0.2), 2)
            impuesto_total = round(monto_total * rd.uniform(0.1, 0.2), 2)           
            descuento_total = round(rd.uniform(monto_total * 0.1, monto_total * 0.3), 2)
            monto_total = round(monto_total + costo_envio + impuesto_total - descuento_total, 2)
                #print(type(codigos_p))
            cursor.execute(f"UPDATE pedido SET monto_total = {monto_total}, costo_envio = {costo_envio}, impuesto_total = {impuesto_total}, descuento_total = {descuento_total} WHERE codigo = '{pedidocodigo}';")
            #else:
                #cursor.execute(f"DELETE FROM pedido WHERE codigo ='{codigos_p}';")
            i += 1
        except Exception as e:
            print(e, i)

#insert_into_table_pedido(1000)

def insert_into_table_comentarioProducto(n):
    ids = rd.sample([x for x in range(10000000, 99999999)], 1000)
    cursor.execute("SELECT id FROM cliente;")
    ids_cliente = cursor.fetchall()
    cursor.execute("SELECT id FROM producto;")
    ids_producto = cursor.fetchall()
    i = 0
    while i < n:
        try:
            id = ids[i]
            clienteid = rd.choice(ids_cliente)[0]
            fecha = str(radar.random_datetime(start = datetime.date.fromisoformat('2019-04-11'), stop = datetime.date(year=2022, month=11, day=20)))
            texto = get_random_text(50)
            idioma = rd.choice(['Spanish', 'English'])
            productoid = rd.choice(ids_producto)[0]
            cursor.execute(f"INSERT INTO comentarioproducto (id, clienteid, fecha, texto, idioma, productoid) VALUES ({id}, {clienteid}, '{fecha}', '{texto}', '{idioma}', {productoid});")
            i += 1
        except Exception as e:
            print(e, i)


def insert_into_table_contieneP(n):
    cursor.execute("SELECT id FROM producto;")
    producto_id = cursor.fetchall()
    cursor.execute("SELECT codigo FROM pedido;")
    codigo_pedido = cursor.fetchall()
    codigo_pedido = [x[0] for x in codigo_pedido]
    codigo_pedido = codigo_pedido + codigo_pedido + random.choices(codigo_pedido, k = n-(2*len(codigo_pedido))) 
    #print(codigo_pedido)
    i = 0
    while(i < n):
        try:
            pedidocodigo = codigo_pedido[i] 
            productoid = rd.choice(producto_id)[0] 
            cursor.execute(f"SELECT precio FROM producto WHERE id={productoid};") 
            precio_producto_by_id = cursor.fetchone()
            descuentoproducto = round(rd.uniform(precio_producto_by_id[0] * 0.05, precio_producto_by_id[0] * 0.1), 2)
            cantidad = rd.randint(1, 20);
            subtotal = round((precio_producto_by_id[0] - descuentoproducto) * cantidad, 2)
            cursor.execute(f"INSERT INTO contienep(productoid, pedidocodigo, subtotal, cantidad, descuentoproducto) VALUES({productoid}, '{pedidocodigo}', {subtotal}, {cantidad}, {descuentoproducto});")
            i += 1;
        except Exception as e:
            print(e, i)

def insert_into_table_producto(n):
    ids = rd.sample([x for x in range(10000000, 99999999)], n)
    marcas = ["Speackers", "Renzo Costa", "Win Sports", "Capittana", "Lalalove", "Butrich", "Nebula", "Camote Soup", "Agua Clara", "Peruvian Flake", "Quimera", "Sophie", "Crown", "Ayni", "Adidas", "Nike", "Burberry", "Dolce & Gabbana", "Valentino", "Givenchy", "Balenciaga", "Prada", "Versace", "Gucci", "Christian Dior", "Baiter"]
    materiales = ["Algodon", "Poliester", "Lino", "Lana", "Seda", "Nylon", "Lycra", "Cuero", "Fibras sinteticas", "Popelin", "Tejidos mixtos", "Kashmir"]
    i = 0
    while (i < n):
        try:
            id = ids[i]
            descripcion = get_random_text_min_max(40, 60)
            sku = get_random_code(8)
            marca = rd.choice(marcas)
            talla = str(rd.randint(20, 89))
            nombre = get_random_text(15, 25) 
            precio = round(rd.uniform(30.5, 800.5), 2)
            material = rd.choice(materiales)
            stock = rd.randint(5, 150)
            imagen = get_random_string(30, 40)
            cursor.execute(f"INSERT INTO producto(id, descripcion, sku, marca, talla, nombre, precio, material, stock, imagen) VALUES({id}, '{descripcion}', '{sku}', '{marca}', '{talla}', '{nombre}', {precio}, '{material}', {stock}, '{imagen}');")
        except Exception as e:
            print(e, i)


#insert_into_table_contieneP(1500)
#insert_into_table_contieneP(2000)
update_table_pedido()
#insert_into_table_contieneP(1500)
# insert_into_table_pedido(500)