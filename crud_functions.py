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



