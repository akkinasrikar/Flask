import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager=LoginManager()


app = Flask(__name__)

app.config['SECRET_KEY']='aibasics'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view="login"

from myproject.pilots.views import pilots_blueprints
from myproject.company.views import company_blueprints
from myproject.aircraft.views import aircraft_blueprints
from myproject.airport.views import airport_blueprints

app.register_blueprint(company_blueprints,url_prefix='/company')
app.register_blueprint(pilots_blueprints,url_prefix='/pilots')
app.register_blueprint(aircraft_blueprints,url_prefix='/aircraft')
app.register_blueprint(airport_blueprints,url_prefix='/airport')



