from flask import render_template, Blueprint
from flask_login import login_required

carbon_app = Blueprint("carbon_app", __name__)

@carbon_app.route("/carbon_app")
@login_required
def carbon_app_home():
    return render_template("carbon_app/carbon_app.html", title="carbon_app")

@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus')


@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    return render_template('carbon_app/new_entry_car.html', title='new entry car')    


@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane')  


@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry')     


@carbon_app.route('/carbon_app/new_entry_motorcycle', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    return render_template('carbon_app/new_entry_motorcycle.html', title='new entry motorcycle') 


@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle')

@carbon_app.route('/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    return render_template('carbon_app/new_entry_train.html', title='new entry train')


@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk')