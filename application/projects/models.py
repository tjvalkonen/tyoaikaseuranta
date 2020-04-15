from application import db
from application.models import Base

from sqlalchemy.sql import text

class Project(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False

    # Lasketaan yhteen kaikki projektissa toteutunut työ
    @staticmethod
    def work_done_in_project(project_id):
        stmt = text("SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Actual'").params(project_id=project_id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"time":row[0]})

        return response

    # Lasketaan yhteen kaikki projektin arvioitu työ
    @staticmethod
    def work_estimated_in_project(project_id):
        stmt = text("SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Estimate'").params(project_id=project_id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"time":row[0]})

        return response
