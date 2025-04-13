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
        'Motorcycle':{'Gasoline':0.103},
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
        'Motorcycle':{'Gasoline':0,'No Fossil Fuel':0},
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
    entries = Transport.query.filter_by(user_id=current_user.id).all()
    return render_template("carbon_app/your_data.html", title='Your Data', entries=entries)

@carbon_app.route("/carbon_app/delete_emission/<int:entry_id>")
@login_required
def delete_emission(entry_id):
    print(entry_id)
    entry = Transport.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect('/carbon_app/your_data')

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
        transport = 'motorcycle'
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