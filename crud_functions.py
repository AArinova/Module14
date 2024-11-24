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
     cursor.execute('INSERT INTO "Users" ("username", "email", "age", "balance") VALUES ("' + username + '","' + email + '","' + age + '", 1000)')
     connection.commit()
     connection.close()

def is_included(username):
     connection = sqlite3.connect("crud.db")
     cursor = connection.cursor()
     cursor.execute('SELECT "id" FROM Users WHERE "username"="'+username+'"')
     connection.commit()
     users_list = cursor.fetchall()
     connection.close()
     if len(users_list) == 0:
          return False
     else:
          return True


