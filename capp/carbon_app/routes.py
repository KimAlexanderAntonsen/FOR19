from flask import render_template, Blueprint, request, redirect, url_for, flash, abort
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorcycleForm, BicycleForm, WalkForm, TrainForm
import json

carbon_app = Blueprint("carbon_app", __name__)

efco2={
        'Walk':{'No Fossil Fuel':0},
        'Bicycle':{'No Fossil Fuel':0},
        'Car':{'Petrol': 0.160, 'Diesel':0.170,'Electric':0.0193,'Hybrid':0.1261},
        'Motorcycle':{'Small':0.08277,'Medium':0.10086,'Large':0.13237},
        'Bus':{'Diesel':0.027,'Electric':0.013},
        'Train':{'Norway':0.010,'EU':0.033},
        'Ferry':{'Diesel':0.377},
        'Plane':{'Short-haul':0.246,'Long-haul':0.147},
    }

efch4={
        'Walk':{'No Fossil Fuel':0},
        'Bicycle':{'No Fossil Fuel':0},
        'Car':{'Petrol': 0, 'Diesel':0,'Electric':0,'Hybrid':0},
        'Motorcycle':{'Small':0,'Medium':0,'Large':0},
        'Bus':{'Diesel':0,'Electric':0},
        'Train':{'Norway':0,'EU':0},
        'Ferry':{'Diesel':0},
        'Plane':{'Short-haul':0,'Long-haul':0},
     }

@carbon_app.route("/carbon_app")
@login_required
def carbon_app_home():
    return render_template("carbon_app/carbon_app.html", title="carbon_app")

# New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        kms = request.form['kms']
        fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        try:
            db.session.add(emissions)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
        return redirect(url_for('carbon_app.your_data'))
    else:
        print('nono')
    
    return render_template('carbon_app/new_entry_bus.html', 
        title='new entry bus', form=form)

# New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

#New entry ferry
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)     

#New entry motorcycle
@carbon_app.route('/carbon_app/new_entry_motorcycle', methods=['GET','POST'])
@login_required
def new_entry_motorcycle():
    form = MotorcycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorcycle'  # Changed from lowercase 'motorcycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_motorcycle.html', title='new entry motorcycle', form=form) 

#New entry bicycle
@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry train
@carbon_app.route('/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_train.html', title='new entry train', form=form)


#New entry walk
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk', form=form)

@carbon_app.route("/carbon_app/your_data")
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    
    #Emissions by category
    transport_types = ['Bicycle', 'Bus', 'Car', 'Ferry', 'Motorcycle', 'Plane', 'Train', 'Walk']
    emission_transport = [0] * 8
    kms_transport = [0] * 8
    transport_indices = {
        'Bicycle': 0,
        'Bus': 1, 
        'Car': 2,
        'Ferry': 3,
        'Motorcycle': 4,
        'Plane': 5,
        'Train': 6,
        'Walk': 7
    }

    emissions_by_transport = db.session.query(db.func.sum(Transport.total), Transport.transport).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    for transport in transport_types:
        if transport in second_tuple_elements:
            index = second_tuple_elements.index(transport)
            emission_transport[transport_indices[transport]] = first_tuple_elements[index]

    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(Transport.kms), Transport.transport).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    for transport in transport_types:
        if transport in second_tuple_elements:
            index = second_tuple_elements.index(transport)
            kms_transport[transport_indices[transport]] = first_tuple_elements[index]

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(Transport.total), Transport.date).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date).\
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      

    return render_template('carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
@login_required  # Add login required
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    if entry.author != current_user:  # Add user verification
        abort(403)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))  # Use url_for instead of direct path