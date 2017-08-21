import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.moment import Moment

basedir= os.path.abspath(os.path.dirname(__file__))

#configure database
app= Flask(__name__)
app.config['SECRET_KEY'] = '\x05\xa5\xa6\xb8\xe8\x06\x0f\xa9\x98\xf4\xf8\xe5H\x92j9\xab\x16\xe5\xe0\xa8\x9e\xb9\x92'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'thermos.db')
app.config['DEBUG']= True
db = SQLAlchemy(app)


#configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
#to redirect when no logged in
login_manager.login_view = "login"
login_manager.init_app(app)

# for displaying timestamps
moment = Moment(app)

import models
import views