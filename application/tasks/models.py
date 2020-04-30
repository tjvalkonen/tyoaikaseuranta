from application import db
from application.models import Base

from sqlalchemy.sql import text

class Task(Base):

    tasktype = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    # date = db.Column(db.Integer, nullable=False)
    taskstatus = db.Column(db.String(144), nullable=False)

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
                           nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, tasktype):
        self.tasktype = tasktype

    # Haetaan kaikki projektissa tehdyt työt
    @staticmethod
    def find_tasks_in_project(project_id):
        stmt = text("SELECT Task.id, Task.tasktype, Task.description, Task.time, Task.taskstatus, Task.project_id FROM Task WHERE Task.project_id = :project_id").params(project_id=project_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "tasktype":row[1], "description":row[2], "time":row[3], "taskstatus":row[4], "project_id":row[5]})

        return response

