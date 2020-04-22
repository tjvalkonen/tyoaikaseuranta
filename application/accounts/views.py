from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User

@app.route("/accounts", methods=["GET"])
@login_required
def accounts_index():
    return render_template("accounts/list.html", accounts = User.query.all())

# @app.route("/projects/<project_id>/", methods=["POST"])
# @login_required
# def projects_set_done(project_id):

#    t = Project.query.get(project_id)
#    t.done = True
#    db.session().commit()
  
#    return redirect(url_for("projects_index"))

@app.route("/accounts/<account_id>/delete/", methods=["POST"])
@login_required(role="ADMIN")
def accounts_delete(account_id):

    t = User.query.get(account_id)
    db.session.delete(t)
    db.session().commit()
  
    return redirect(url_for("accounts_index"))
