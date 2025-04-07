from flask import render_template, Blueprint

login = Blueprint("login", __name__)
register = Blueprint("register", __name__)

@login.route("/login")
def login_home():
    return render_template("user/login.html", title="login")

@register.route("/register")
def register_home():
    return render_template("user/register.html", title="register")