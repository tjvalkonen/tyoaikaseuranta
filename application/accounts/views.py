from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import ModifyAccountForm

@app.route("/accounts", methods=["GET"])
@login_required
def accounts_index():
    return render_template("accounts/list.html", accounts = User.query.all())

@app.route("/accounts/<account_id>/delete/", methods=["POST"])
@login_required(role="ADMIN")
def accounts_delete(account_id):

    a = User.query.get(account_id)
    db.session.delete(a)
    db.session().commit()
  
    return redirect(url_for("accounts_index"))

@app.route("/accounts/<account_id>/", methods=["GET"])
@login_required()
def accounts_modify_form(account_id):
  
    return render_template("accounts/modifyAccount.html", account_id = account_id, form = ModifyAccountForm(), projects = User.workdone_in_projects())

@app.route("/accounts/<account_id>/modify", methods=["POST"])
@login_required()
def accounts_modify(account_id):
    form = ModifyAccountForm(request.form)

    if not form.validate():
        return render_template("accounts/modifyAccount.html", form = form)

    a = User.query.get(account_id)
    a.name = form.name.data
    a.username = form.username.data
    a.password = form.password.data
    a.role = form.role.data

    db.session().commit()
  
    return redirect(url_for("accounts_modify_form" , account_id = account_id))

