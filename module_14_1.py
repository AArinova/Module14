import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE "Users" (
        "id"	INTEGER UNIQUE,
        "username"	TEXT NOT NULL,
        "email "	TEXT NOT NULL,
        "age"	INTEGER,
        "balance"	INTEGER
    )
""")
connection.commit()
connection.close()

#print("Hello")