from application import db
from application.models import Base
from flask_login import current_user

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)

    projects = db.relationship("Project", backref='account', lazy=True)

    tasks = db.relationship("Task", backref='account', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [self.role]

    @staticmethod
    def workdone_in_projects():
        stmt = text("SELECT Project.id, Project.name, Project.done, SUM(Task.time) FROM Project"
                     " LEFT JOIN Task ON Task.project_id = Project.id"
                     " WHERE (Task.taskstatus IS 'Actual') AND (Task.account_id = :current_user_id)"
                     " GROUP BY Project.id").params(current_user_id=current_user.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "done":row[2], "time":row[3]})

        return response
