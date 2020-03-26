from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.projects.models import Project
from application.projects.forms import ProjectForm

@app.route("/projects", methods=["GET"])
def projects_index():
    return render_template("projects/list.html", projects = Project.query.all())

@app.route("/projects/new/")
@login_required
def projects_form():
    return render_template("projects/new.html", form = ProjectForm())

@app.route("/projects/<project_id>/", methods=["POST"])
@login_required
def projects_set_done(project_id):

    t = Project.query.get(project_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("projects_index"))

@app.route("/projects/", methods=["POST"])
@login_required
def projects_create():
    form = ProjectForm(request.form)
#    p = Project(request.form.get("name"))

    if not form.validate():
        return render_template("projects/new.html", form = form)

    p = Project(form.name.data)
    p.done = form.done.data
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("projects_index"))
