from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = '9aad4163fdb903e924e956c2152ef40a1d44'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bwjuhsexzwtzhd:0199895fc234163d0ff6110bee45109652094462ea7131513ce496106c62509d@ec2-34-231-177-125.compute-1.amazonaws.com:5432/d68f3fa1hfjrcn'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import main




























