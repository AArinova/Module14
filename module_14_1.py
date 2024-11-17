import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE "Users" (
        "id"	INTEGER UNIQUE,
        "username"	TEXT NOT NULL,
        "email"	TEXT NOT NULL,
        "age"	INTEGER,
        "balance"	INTEGER
    )
""")
connection.commit()

for num in range(1, 11):
    insert_str = '("User' + str(num) + '", "example1@gmail.com", '+str(num*10) + ', 1000)'
    requery_str = 'INSERT INTO "Users" ("username", "email", "age", "balance") VALUES ' + insert_str
    print(requery_str)
    cursor.execute(requery_str)
    connection.commit()

connection.close()

