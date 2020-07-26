from flask_restful import Api, Resource
from flask import Flask,request
from userregister import UserRegister
import jwt
import sqlite3

app=Flask(__name__)
api=Api(app)


class Item(Resource):
    def get(self,name):
        connection=sqlite3.connect("data.db")
        cursor=connection.cursor()
        query="Select * from items where item=?"
        row=cursor.execute(query,(name,)).fetchone()
        if row:
            return "Item  {item} Price  {price}".format(item=row[1], price=row[2])
        else:
            return "Item {item} not found".format(item=name)

''''
    def delete(self, name):
      for item in items:
          if item['name']==name:
              items.remove(item)
              return "Deleted"

    def put(self, name):
      data = request.get_json()
      for item in items:
           if item['name'] == name:
              item['price']=data['price']
              return item

'''
class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        select_items = "Select * from items"
        for row in cursor.execute(select_items):
            dict={}
            dict.
            return "Item: {item}, price:{price}".format(item=row[1],price=row[2])

    def post(self):
        data = request.get_json()
        item = {'name': data['name'], 'price': data['price']}
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "Select * from items where item=?"
        row = cursor.execute(query, (data['name'],)).fetchone()
        if row:
            return "Item {item} already exist".format(item=data['name'])
        else:
            query = "insert into items values (NULL,?,?)"
            cursor.execute(query, (data['name'],data['price']))
            return "Item {item} has been inserted".format(item=data['name'])
        return item, 201


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/item')
api.add_resource(UserRegister,'/register')
app.run(port=8000)
_