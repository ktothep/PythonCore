from flask_restful import Api, Resource
from flask import Flask,request
from userregister import UserRegister
import jwt

app=Flask(__name__)
api=Api(app)

items=[]
class Item(Resource):
    def get(self,name):
       for item in items:
           if item['name']==name:
               return item,200
       return ("Item not Found"),404


    def post(self,name):
        data= request.get_json()
        item={'name':name,'price':data['price']}
        items.append(item)
        return item,201

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


class ItemList(Resource):
    def get(self):
         return items

    def post(self):
        data = request.get_json()
        item = {'name': data['name'], 'price': data['price']}
        items.append(item)
        return item, 201


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/item')
api.add_resource(UserRegister,'/register')
app.run(port=8000)
_