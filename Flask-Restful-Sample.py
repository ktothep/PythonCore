from flask_restful import Api, Resource
from flask import Flask

app=Flask(__name__)
api=Api(app)

class Student(Resource):
    def get(self,name):
       return {'student':name}

api.add_resource(Student,'/student/<string:name>')
app.run(port=8000)


