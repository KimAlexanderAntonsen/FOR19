from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


application = Flask(__name__)


#application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'
application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
#DBVAR = 'postgresql://postgres:CarbonTrace1122!@awseb-e-4det36zmw7-stack-awsebrdsdatabase-gcy7fqy6etuj.cpmus8seyhmx.eu-north-1.rds.amazonaws.com:5432/ebdb'
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'login.login_home'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.user.routes import login
from capp.user.routes import register


application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(login)
application.register_blueprint(register)
