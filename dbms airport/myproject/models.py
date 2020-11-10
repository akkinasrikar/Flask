from myproject import db
from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

class User(db.Model,UserMixin):

	__tablename__ = 'users'

	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(64),unique=True,index=True)
	username = db.Column(db.String(64),unique=True,index=True)
	password_hash = db.Column(db.String(128))

	def __init__(self,email,username,password):
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)
	def check_password(self,password):
		return check_password_hash(self.password_hash,password)

class Pilot(db.Model):

	__tablename__ = 'pilots'

	id = db.Column(db.Integer,primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	age = db.Column(db.Integer)
	rank = db.Column(db.Integer)
	company = db.relationship('Company',backref='pilot',uselist=False)

	def __init__(self,first_name,last_name,age,rank):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.rank = rank

	def __repr__(self):
		if self.company:
			return f"Pilot name is {self.first_name} {self.last_name} and company is {self.company.name}"
		else:
			return f"Pilot name is {self.first_name} {self.last_name} and has no company assigned yet."

class Company(db.Model):

    __tablename__ = 'company'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    pilot_id = db.Column(db.Integer,db.ForeignKey('pilots.id'))
    company_owns=db.relationship('Aircraft',backref='aircrafts',uselist=False)
    
    def __init__(self,name,pilot_id):
        self.name = name
        self.pilot_id = pilot_id
    def __repr__(self):
    	return f"Company name is {self.name}"

class Aircraft(db.Model):

	__tablename__ = 'aircraft'

	call_sign=db.Column(db.String, primary_key=True)
	model_no=db.Column(db.String)
	turn_around_count=db.Column(db.Integer)
	sc= db.Column(db.String)
	ds= db.Column(db.String)
	emergency=db.Column(db.Boolean)
	altitude=db.Column(db.Integer)
	pilot=db.Column(db.Integer,db.ForeignKey('pilots.id'))
	distance=db.Column(db.Integer)
	crash=db.Column(db.Boolean)
	company=db.Column(db.Text, db.ForeignKey('company.id'))
	speed=db.Column(db.Integer)
	delay=db.Column(db.Integer)

	def __init__(self,call_sign,model_no,turn_around_count,sc,ds,emergency,altitude,pilot,distance,crash,company,speed,delay):
		self.call_sign=call_sign
		self.model_no=model_no
		self.turn_around_count=turn_around_count
		self.sc=sc
		self.ds=ds
		self.emergency=emergency
		self.altitude=altitude
		self.pilot=pilot
		self.distance=distance
		self.crash=crash
		self.company=company
		self.speed=speed
		self.delay=delay

	def __repr__(self):
		return f"{self.call_sign} {self.model_no} {self.turn_around_count} {self.sc} {self.ds} {self.emergency} {self.altitude} {self.pilot} {self.distance} {self.crash} {self.company} {self.speed} {self.delay} "

class Airport(db.Model):

	__tablename__ = 'airport'

	icao=db.Column(db.String,primary_key=True)
	tk=db.Column(db.Integer)
	ld=db.Column(db.Integer)
	tx=db.Column(db.Integer)
	rw=db.Column(db.Integer)
	ps=db.Column(db.Integer)

	def __init__(self,icao,tk,ld,tx,rw,ps):
		self.icao=icao
		self.tk=tk
		self.ld=ld
		self.tx=tx
		self.rw=rw
		self.ps=ps
	def __repr__(self):
		return f"{self.icao} {self.tk} {self.ld} {self.tx} {self.rw} {self.ps}"



				




