from flask import render_template, Blueprint
from flask_login import login_required

carbon_app = Blueprint("carbon_app", __name__)

@carbon_app.route("/carbon_app")
@login_required
def carbon_app_home():
    return render_template("carbon_app/carbon_app.html", title="carbon_app")