from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import AccountForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new", methods=["GET", "POST"])
# @login_required
def accounts_create():
    form = AccountForm(request.form)

    if not form.validate():
        return render_template("auth/newAccount.html", form = form)

    a = User(form.name.data)
    a.username = form.username.data
    a.password = form.password.data

    db.session().add(a)
    db.session().commit()
  
    return redirect(url_for("index"))
