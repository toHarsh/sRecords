from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY']=os.environ.get('API_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(' SQLALCHEMY_DATABASE_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

login_manager = LoginManager(app)

from SIS.routes import sis

app.register_blueprint(sis)
