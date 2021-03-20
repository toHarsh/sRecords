from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)

# app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
app.config['SECRET_KEY']="8a62b083c268dfcf91b523a0b5eb9f08"
app.config['SQLALCHEMY_DATABASE_URL'] = os.environ.get('DATABASE_URL')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

login_manager = LoginManager(app)

from SIS.routes import sis

app.register_blueprint(sis)
