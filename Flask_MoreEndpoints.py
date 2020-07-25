from flask import Flask,jsonify,request
from flask_restful import Api, Resource

store=Flask(__name__)

stores=[
  {
    'name':'Store 1',
        'items': [
                {
                    'name':'Lamp',
                    'price':10.00
                }
            ]
    }
]


@store.route('/store',methods=['POST'])
def createStore():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(stores)


@store.route('/store',)
def getallStore():

    return jsonify({'store':stores})

@store.route('/store/<string:name>')
def getStore(name):
    print(len(stores))
    for store in stores:
            if store['name'] == name :
             return jsonify(store)


@store.route('/store/<string:name>/item',methods=['POST'])
def createItem(name):
    request_data=request.get_data();
    for store in stores:
        if store['name'] == name:
           new_item={
               'name':request_data['name'],
               'price':request_data['price']

           }
           store['items'].append(new_item)
           return jsonify(new_item)
        else:
            return "Item not found"

@store.route('/store/<string:name>/item',methods=['GET'])
def getItem(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
        else:
            return "Item not found"

store.run(port=8000)