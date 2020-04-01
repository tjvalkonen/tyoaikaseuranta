from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm

# haetaan listaan kaikki projektissa tehdyt työt
@app.route("/tasks/<project_id>", methods=["GET"])
@login_required
def tasks_index(project_id):
    return render_template("tasks/list.html", tasks = Task.find_tasks_in_project(project_id), project_id = project_id, form = TaskForm())

# @app.route("/tasks/<project_id>/new/")
# @login_required
# def tasks_form(project_id):
#     return render_template("tasks/new.html", form = TaskForm())

# @app.route("/tasks/<project_id>/<task_id>/", methods=["POST"])
# @login_required
# def tasks_update(task_id):

#     t = Task.query.get(task_id)
    # t.time = True
#     db.session().commit()
  
#     return redirect(url_for("tasks_index"))

# @app.route("/tasks/<project_id>/<task_id>/delete/", methods=["POST"])
# @login_required
# def tasks_delete(task_id):

#    t = Project.query.get(task_id)
#    db.session.delete(t)
#    db.session().commit()
  
#    return redirect(url_for("tasks_index"))

# @app.route("/tasks")
@app.route("/tasks", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)
    project_id=request.args.get('project_id')

    if not form.validate():
        return render_template("tasks/list.html", tasks = Task.find_tasks_in_project(project_id), project_id = project_id, form = form)

    t = Task(form.taskType.data)
    t.description = form.description.data
    t.time = form.time.data
    t.project_id = project_id
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for('tasks_index', project_id=project_id))
