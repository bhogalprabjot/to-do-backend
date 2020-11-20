from db import db

class TaskModel(db.Model):
    __tablename__ = 'task'
    
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80))
    isDone = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, label, isDone=False):
        self.label = label
        self.isDone = isDone
    
    def json(self):
        return {'task': 
            {
                'id': self.id,
                'label': self.label,
                'is_done': self.isDone        
            }
        }
    @classmethod
    def get_by_id(cls, task_id):
        return cls.query.filter_by(id=task_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
