from flask import render_template, Blueprint, request, redirect, url_for, flash, abort
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorcycleForm, BicycleForm, WalkForm, TrainForm
import json

carbon_app = Blueprint("carbon_app", __name__)

efco2={
    'Walk': {'Human powered': 0.0},
    'Bicycle': {'Human powered': 0.0},
    'Car': {
        'Petrol': 0.160,
        'Diesel': 0.170,
        'Electric': 0.0193,
        'Hybrid': 0.1261
    },
    'Motorcycle': {
        'Small': 0.08277,
        'Medium': 0.10086,
        'Large': 0.13237
    },
    'Bus': {
        'Diesel': 0.027,
        'Electric': 0.013
    },
    'Train': {
        'Norway': 0.010,
        'EU': 0.033
    },
    'Ferry': {'Diesel': 0.377},
    'Plane': {
        'Short-haul': 0.246,
        'Long-haul': 0.147
    }
}

@carbon_app.route("/carbon_app")
@login_required
def carbon_app_home():
    return render_template("carbon_app/carbon_app.html", title="carbon_app")

def handle_new_entry(form, transport):
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template(f'carbon_app/new_entry_{transport.lower()}.html', title=f'new entry {transport.lower()}', form=form)

@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    return handle_new_entry(BusForm(), 'Bus')

@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    return handle_new_entry(CarForm(), 'Car')

@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    return handle_new_entry(PlaneForm(), 'Plane')

@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    return handle_new_entry(FerryForm(), 'Ferry')

@carbon_app.route('/carbon_app/new_entry_motorcycle', methods=['GET','POST'])
@login_required
def new_entry_motorcycle():
    return handle_new_entry(MotorcycleForm(), 'Motorcycle')

@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    return handle_new_entry(BicycleForm(), 'Bicycle')

@carbon_app.route('/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    return handle_new_entry(TrainForm(), 'Train')

@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    return handle_new_entry(WalkForm(), 'Walk')

@carbon_app.route("/carbon_app/your_data")
@login_required
def your_data():
    entries = Transport.query.filter_by(author=current_user).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()

    transport_types = ['Bicycle', 'Bus', 'Car', 'Ferry', 'Motorcycle', 'Plane', 'Train', 'Walk']
    emission_transport = [0] * 8
    kms_transport = [0] * 8
    transport_indices = {name: i for i, name in enumerate(transport_types)}

    emissions_by_transport = db.session.query(db.func.sum(Transport.co2), Transport.transport).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    for total, transport in emissions_by_transport:
        if transport in transport_indices:
            emission_transport[transport_indices[transport]] = total

    kms_by_transport = db.session.query(db.func.sum(Transport.kms), Transport.transport).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    for total, transport in kms_by_transport:
        if transport in transport_indices:
            kms_transport[transport_indices[transport]] = total

    emissions_by_date = db.session.query(db.func.sum(Transport.co2), Transport.date).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_emissions = [total for total, _ in emissions_by_date]
    dates_label = [date.strftime("%m-%d-%y") for _, date in emissions_by_date]

    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_kms = [total for total, _ in kms_by_date]

    return render_template('carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
@login_required
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    if entry.author != current_user:
        abort(403)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
