import flask
import os
import flask_login
from flask_session import Session
from flask import send_from_directory, request, session, jsonify

app = flask.Flask(__name__)
app.secret_key = "s_key"     # Secret key for sessions

## Flask login initialisations
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.session_protection = None


DEV_PORT = 5000  # Dev port
PRO_PORT = 80    # Production default port

DEV_HOST = 'localhost' # Dev host
PRO_HOST = '0.0.0.0'   # Production default host

# An attempt to limit SQL connetion reset
SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True, 
        "pool_recycle": 300 }



##### SETTINGS ######
#mode = 'production'
mode = 'development'

#db_mode = 'production'
db_mode = 'development'

# Google Login settings

# Database settings






" Session initialisations"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)