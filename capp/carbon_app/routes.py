from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorcycleForm, BicycleForm, WalkForm, TrainForm
from capp.models import Transport
from capp import db

carbon_app = Blueprint("carbon_app", __name__)

efco2={
        'Walk':{'No Fossil Fuel':0},
        'Bicycle':{'No Fossil Fuel':0},
        'Ferry':{'Diesel':0.019},
        'Train':{'Diesel':0.041,'Electric':0},
        'Car':{'Diesel':0.171, 'Gasoline':0.192, 'Hybrid':0.109, 'Electric':0.053},
        'Motorbike':{'Gasoline':0.103},
        'Bus':{'Diesel':0.105,'Electric':0},
        'Long distance flight':{'Jet Fuel':0.150},
        'Domestic flight':{'Jet Fuel':0.255},
        'Light rail and tram':{'Electric':0.035}
    }

efch4={
        'Walk':{'No Fossil Fuel':0},
        'Bicycle':{'No Fossil Fuel':0},
        'Ferry':{'Diesel':0},
        'Train':{'Diesel':0,'Electric':0},
        'Car':{'Diesel':0, 'Gasoline':0, 'Hybrid':0, 'Electric':0},
        'Motorbike':{'Gasoline':0,'No Fossil Fuel':0},
        'Bus':{'Diesel':0,'Electric':0},
        'Long distance flight':{'Jet Fuel':0},
        'Domestic flight':{'Jet Fuel':0},
        'Light rail and tram':{'Electric':0}
     }

@carbon_app.route("/carbon_app")
@login_required
def carbon_app_home():
    return render_template("carbon_app/carbon_app.html", title="carbon_app")

@carbon_app.route("/carbon_app/your_data")
@login_required
def your_data():
    return render_template("carbon_app/your_data.html", title='Your Data')

@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
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
        print('Dette funket!')
        return redirect(url_for('carbon_app.your_data'))
    else:
        print('nono')
    
    return render_template('carbon_app/new_entry_bus.html', 
        title='new entry bus', form=form)

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