from flask_restful import Resource, reqparse
from models.task import TaskModel

class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
    required=True,
    )

    def post(self):
        req_data = Task.parser.parse_args()
        task = TaskModel(**req_data)
        return task.json(), 201
