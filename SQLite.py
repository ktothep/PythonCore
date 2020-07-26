import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()
create_user="create table users(id INTEGER PRIMARY KEY,username text,password text)"
create_item="create table items(id INTEGER PRIMARY KEY,item text,price text)"
cursor.execute(create_user)
cursor.execute(create_item)

insert_user="Insert into users values(NULL,?,?)"
insert_item="Insert into items values(NULL,?,?)"
users=[
    ('User1','Pass1'),
    ('User2', 'Pass2'),
    ('User3', 'Pass3')
]
items=[
    ('Item1','10'),
    ('Item2', '20'),
    ('Item3', '30')
]
cursor.executemany(insert_user,users)
cursor.executemany(insert_item,items)
select_user="Select * from users"
select_items="Select * from items"

for row in cursor.execute(select_user):
    print(row)
for row in cursor.execute(select_items):
    print(row)
connection.commit()
connection.close()


