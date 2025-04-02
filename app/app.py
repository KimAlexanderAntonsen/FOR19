from config import *
from flask import redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user
from config import db, bcrypt
from models import User


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/methodology')
def methodology():
    return flask.render_template('methodology.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user_hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        user = User(username=username, email=email, password=user_hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
    return flask.render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form['email']
        user_hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, user_hashed_password):
            login_user(user)
            next_page = request.args.get('next')
            flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home.home_home'))
        else:
            flash('Login Unsuccessful. Please check email and password!', 'danger') 
    return flask.render_template('login.html')

@app.route('/calculator')
def calculator():
    return flask.render_template('calculator.html')

## User handling
@login_manager.user_loader
def load_user(userid):
    return "User 1"

@app.errorhandler(404)
def not_found(e): 
    return flask.render_template('404.html') 

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    if (mode == 'production'):
        app.run(port=PRO_PORT, host=PRO_HOST, debug = False)
    if (mode == 'development'):
        app.run(port=DEV_PORT, host=DEV_HOST, debug=True)