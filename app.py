from flask import Flask
from flask_restful import Api, Resource
from resources.task import Task
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Task, '/task', '/task/<int:id>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)





# class HelloWorld(Resource):
#     def get(self):
#         return {'message': 'Hello World'}

# api.add_resource(HelloWorld, '/')