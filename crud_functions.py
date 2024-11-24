import sqlite3

def initiate_db():
     connection = sqlite3.connect("crud.db")
     cursor = connection.cursor()
     cursor.execute("""
          CREATE TABLE "Products" (
              "id"	INTEGER,
              "title"	TEXT NOT NULL, 
              "description"	TEXT,
              "price"	INTEGER NOT NULL,
              PRIMARY KEY("id")
          );
      """)
     connection.commit()
     connection.close()

def get_all_products():
     connection = sqlite3.connect("crud.db")
     cursor = connection.cursor()
     cursor.execute("SELECT * FROM 'Products'")
     products = cursor.fetchall()
     connection.commit()
     connection.close()
     return products

def add_user(username, email, age):
     connection = sqlite3.connect("crud.db")
     cursor = connection.cursor()
     cursor.execute('INSERT INTO "Users" ("username", "email", "age", "balance") VALUES ("' + username + '","' + email + '", "' + age + '", 1000)')
     connection.commit()
     connection.close()

def is_included(username):
     connection = sqlite3.connect("crud.db")
     cursor = connection.cursor()
     cursor.execute('SELECT * FROM Users')
     users_list = cursor.fetchall()
     connection.close()
     print(users_list)
     is_included_flag = False
     for user in users_list:
          if username == user[1]:
               is_included_flag = True
               break
     return is_included_flag



     #принимает имя пользователя и возвращает True,
# если такой пользователь есть в таблице Users, в противном случае False.
# Для получения записей используйте SQL запрос.

