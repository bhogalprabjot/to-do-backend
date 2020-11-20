from flask_restful import Resource


"""
get task/{id}
add task/{id}
"""
class Task(Resource):
    task = []

    def get(self, id):
        

