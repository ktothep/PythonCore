import sqlite3

connection=sqlite3.connect("users.db")
cursor=connection.cursor()
query="Create table users(id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(query)
connection.commit()
connection.close()