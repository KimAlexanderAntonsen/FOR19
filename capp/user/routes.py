from flask import render_template, Blueprint, redirect, flash, url_for, request
from capp.user.forms import RegistrationForm, LoginForm
from capp.models import User
from capp import db, bcrypt
from flask_login import login_user, current_user, logout_user

login = Blueprint("login", __name__)
register = Blueprint("register", __name__)

@register.route("/register", methods=['GET','POST'])
def register_home():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home.home_home'))
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('login.login_home'))
    return render_template("user/register.html", title="register", form=form)


@login.route("/login", methods=['GET','POST'])
def login_home():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home.home_home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            db.session.add(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home.home_home'))
        else:
            flash('Login Unsuccessful. Please check email and password!', 'danger') 
    return render_template('user/login.html', title='login', form=form)


@login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.home_home'))