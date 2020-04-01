from application import db
from application.models import Base

class Task(Base):

    taskType = db.Column(db.String(144), nullable=False)
    descripion = db.Column(db.String(144), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    # date = db.Column(db.Integer, nullable=False)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
                           nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, taskType):
        self.taskType = taskType
