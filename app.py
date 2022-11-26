from dotenv import load_dotenv
load_dotenv()

import os

import flask
import flask_sqlalchemy
import flask_cors

# DB connection URI
db_connection = os.environ.get('DATABASE_URL')

if db_connection.startswith("postgres://"):
    db_connection = db_connection.replace("postgres://", "postgresql://", 1)

# application initialization
application = flask.Flask(__name__)

application.secret_key = b'\xc2\xa4\x9f\xaa\xdf\xdcp\n\x90:O\xfb'
application.config['SQLALCHEMY_DATABASE_URI'] = db_connection
application.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 3600,
}

# Flask SQLAlchemy
db = flask_sqlalchemy.SQLAlchemy()
db.init_app(application)

# Models
from models import *

# Routes
from views import *

# CORS setup
cors = flask_cors.CORS()
cors.init_app(application)

if __name__ == '__main__':
    application.debug = True
    application.run()