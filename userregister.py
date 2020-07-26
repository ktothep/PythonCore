import sqlite3
from flask import request
from flask_restful import Resource
from user import User


def findby_username(username):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    query = "select * from users where username=?"
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    connection.close()
    return row

class UserRegister(Resource):
    def post(self):
        data=request.get_json();
        username=data['username']
        password=data['password']
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        row=findby_username(username)

        if row:
            return "User {user} already exist".format(user=username)
        else:
            query="Insert into users values (NULL,?,?)"
            cursor.execute(query,(username,password))
            connection.commit()
            connection.close()
            return "User {username} created".format(username=username),201

