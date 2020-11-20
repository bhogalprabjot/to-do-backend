from flask_restful import Resource, reqparse
from models.task import TaskModel

class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('label',
    required=True,
    )

    def get(self, id):
        task = TaskModel.get_by_id(id)
        if task:
            return task.json()
        return {'message':'A task with this id does not exist.'}

    def post(self):
        req_data = Task.parser.parse_args()
        task = TaskModel(**req_data)
        task.save_to_db()
        return task.json(), 201
