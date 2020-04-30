from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.projects.models import Project
from application.projects.forms import ProjectForm

@app.route("/projects", methods=["GET"])
@login_required
def projects_index():
    return render_template("projects/list.html", projects = Project.query.all(), work_done_in_projects = Project.projects_list_workdone())

# projects = Project.query.all())

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

@app.route("/projects/<project_id>/delete/", methods=["POST"])
@login_required(role="ADMIN")
def projects_delete(project_id):

    t = Project.query.get(project_id)
    db.session.delete(t)
    db.session().commit()
  
    return redirect(url_for("projects_index"))

@app.route("/projects/", methods=["POST"])
@login_required(role="ADMIN")
def projects_create():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template("projects/new.html", form = form)

    p = Project(form.name.data)
    p.done = form.done.data
    p.account_id = current_user.id

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("projects_index"))
