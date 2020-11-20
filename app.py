from flask import Flask
from flask_restful import Api, Resource
from resources.task import Task


app = Flask(__name__)
api = Api(app)

api.add_resource(Task)

if __name__ == '__main__':
    app.run()





# class HelloWorld(Resource):
#     def get(self):
#         return {'message': 'Hello World'}

# api.add_resource(HelloWorld, '/')