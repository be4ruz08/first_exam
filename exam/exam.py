# Bahodirov Behruz

# 1

# import psycopg2
#
# db_name = 'n47'
# password = '258182126'
# host = 'localhost'
# port = 5432
# user = 'postgres'
#
# def create_table():
#     with psycopg2.connect(dbname=db_name,
#                           user=user,
#                           password=password,
#                           host=host,
#                           port=port) as conn:
#         with conn.cursor() as cur:
#             create_table_query = """create table if not exists Products(
#                 id serial PRIMARY KEY,
#                 name varchar(70) not null,
#                 image varchar(255),
#                 price varchar,
#                 color varchar
#             );
#             """
#             cur.execute(create_table_query)
#             conn.commit()
#             print('Table Successfully Created')

# 2

# def insert_product(name, image, price, color):
#     with psycopg2.connect(dbname=db_name,
#                           user=user,
#                           password=password,
#                           host=host,
#                           port=port) as conn:
#         with conn.cursor() as cur:
#             insert_query = """insert into Products (name, image, price, color)
#                               values (%s, %s, %s, %s) returning id"""
#             cur.execute(insert_query, (name, image, price, color))
#             product_id = cur.fetchone()[0]
#             conn.commit()
#             print('Product Successfully Inserted')
#             return product_id

# def select_all_products():
#     with psycopg2.connect(dbname=db_name,
#                           user=user,
#                           password=password,
#                           host=host,
#                           port=port) as conn:
#         with conn.cursor() as cur:
#             select_query = "SELECT * FROM Products"
#             cur.execute(select_query)
#             products = cur.fetchall()
#             for product in products:
#                 print(product)

# def update_product(product_id, name, image, price, color):
#     with psycopg2.connect(dbname=db_name,
#                           user=user,
#                           password=password,
#                           host=host,
#                           port=port) as conn:
#         with conn.cursor() as cur:
#             update_query = """update Products
#                               set name = %s, image = %s, price = %s, color = %s
#                               where id = %s"""
#             cur.execute(update_query, (name, image, price, color, product_id))
#             conn.commit()
#             print('Product Successfully Updated')

# def delete_product(product_id):
#     with psycopg2.connect(dbname=db_name,
#                           user=user,
#                           password=password,
#                           host=host,
#                           port=port) as conn:
#         with conn.cursor() as cur:
#             delete_query = "DELETE FROM Products WHERE id = %s"
#             cur.execute(delete_query, (product_id,))
#             conn.commit()
#             print('Product Successfully Deleted')


# create_table()
#
# product_id = insert_product("Product 1", "image1.jpg", '15 000', 'red')
#
# select_all_products()
#
#
# update_product(product_id, "Updated Product 1", "updated_image.jpg", 'updated price 10 000', 'updated color blue')
#
# delete_product(product_id)



# 3

# class Alphabet:
#     def __init__(self):
#         self.current_index = 0
#         self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index >= len(self.alphabet):
#             raise StopIteration
#         letter = self.alphabet[self.current_index]
#         self.current_index += 1
#         return letter
#
#
# alphabet = Alphabet()
#
# for letter in alphabet:
#     print(letter)


# 4

# import threading
# import time
#
#
# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)
#
#
# def print_letters():
#     letters = 'ABCDE'
#     for letter in letters:
#         print(letter)
#         time.sleep(1)
#
#
# thread_numbers = threading.Thread(target=print_numbers)
# thread_letters = threading.Thread(target=print_letters)
#
# thread_numbers.start()
# thread_letters.start()
#
#
# thread_numbers.join()
# thread_letters.join()


# 5

# class Product:
#     db_name = 'n47'
#     password = '258182126'
#     host = 'localhost'
#     port = 5432
#     user = 'postgres'
#
#     def __init__(self, name, image, price, color):
#         self.name = name
#         self.image = image
#         self.price = price
#         self.color = color
#
#     def save(self):
#         with psycopg2.connect(dbname=self.db_name,
#                               user=self.user,
#                               password=self.password,
#                               host=self.host,
#                               port=self.port) as conn:
#             with conn.cursor() as cur:
#                 insert_query = """insert into Products (name, image, price, color)
#                                   values (%s, %s, %s, %s)"""
#                 cur.execute(insert_query, (self.name, self.image, self.price, self.color))
#                 conn.commit()
#                 print('Product successfully saved')
#
#
# def save_product():
#     product = Product("Product 2", "image2.jpg", '25 000', 'black')
#     product.save()
#
# save_product()


# 6

# import psycopg2

# class DbConnect:
#     def __init__(self, db_name, user, password, host='localhost', port=5432):
#         self.db_name = db_name
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             dbname=self.db_name,
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             port=self.port
#         )
#         self.cur = self.conn.cursor()
#         return self.conn, self.cur
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.cur:
#             self.cur.close()
#         if self.conn:
#             self.conn.close()


# 7

# import json
# import requests
#
# def save_data():
#     url = "https://dummyjson.com/products/"
#     response = requests.get(url)
#     products = json.loads(response.content)['products']
#
#     with DbConnect(db_name='n47', user='postgres', password='258182126') as (conn, cur):
#         for product in products:
#             if 'color' in product:
#                 cur.execute("""
#                     INSERT INTO products (id, name, price, color)
#                     VALUES (%s, %s, %s, %s)
#                 """, (product['id'], product['title'], product['price'], product['color']))
#             else:
#                 print(product['id'], product['title'])
#         conn.commit()
#
# save_data()


