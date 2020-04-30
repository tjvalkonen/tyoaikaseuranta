from application import db
from application.models import Base
from flask_login import current_user

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

    # Lasketaan yhteen kaikki kirjautuneen käyttäjän projektissa tekemä työ
    @staticmethod
    def work_done_in_project_by_user(project_id):
        stmt = text("SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Actual' AND Task.account_id =:account_id").params(project_id=project_id, account_id=current_user.id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"time":row[0]})

        return response

    # Lasketaan yhteen kaikki kirjautuneen käyttäjän projektiin arvioitu työ
    @staticmethod
    def work_estimated_in_project_by_user(project_id):
        stmt = text("SELECT SUM(Task.time) FROM Task WHERE Task.project_id = :project_id AND Task.taskstatus = 'Estimate' AND Task.account_id =:account_id").params(project_id=project_id, account_id=current_user.id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"time":row[0]})

        return response

    @staticmethod
    def projects_list_workdone():
        stmt = text("SELECT Project.id, Project.name, Project.done, SUM(Task.time) FROM Project"
                     " LEFT JOIN Task ON Task.project_id = Project.id"
                     " WHERE (Task.taskstatus IS 'Actual')"
                     " GROUP BY Project.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "done":row[2], "time":row[3]})

        return response
