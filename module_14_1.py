import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute("""
     CREATE TABLE "Users" (
         "id" INTEGER UNIQUE, 
         "username"	TEXT NOT NULL,
         "email"	TEXT NOT NULL,
         "age"	INTEGER,
         "balance"	INTEGER,
         PRIMARY KEY("id")
     );
 """)
connection.commit()

for num in range(1, 11):
     insert_str = '("User' + str(num) + '", "example1@gmail.com", '+str(num*10) + ', 1000)'
     requery_str = 'INSERT INTO "Users" ("username", "email", "age", "balance") VALUES ' + insert_str
     cursor.execute(requery_str)
     connection.commit()

for num in range(1, 11, 2):
     cursor.execute('UPDATE "Users" SET "balance"= ? WHERE "username"=?', (500, "User"+str(num)))
     connection.commit()

for num in range(1, 11, 3):
     cursor.execute('DELETE FROM Users WHERE username=?', ("User"+str(num),) )
     connection.commit()

cursor.execute('SELECT * FROM "Users" WHERE "age" <> 60')
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")

connection.close()

