from application import db
from application.models import Base

from sqlalchemy.sql import text

class Task(Base):

    taskType = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    # date = db.Column(db.Integer, nullable=False)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
                           nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, taskType):
        self.taskType = taskType

    # Haetaan kaikki projektissa tehdyt työt
    @staticmethod
    def find_tasks_in_project(project_id):
        stmt = text("SELECT Task.id, Task.taskType, Task.description, Task.time FROM Task"
                    " WHERE Task.project_id = project_id")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "taskType":row[1], "description":row[2], "time":row[3]})

        return response
