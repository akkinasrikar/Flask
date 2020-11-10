from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Airport,Aircraft
from flask import request
from myproject.airport.forms import AddForm,SelectForm
import pandas as pd
import numpy as np

airport_blueprints=Blueprint('airport',__name__,template_folder='templates/airport')


icaos=['VIAG', 'VIAM','VIAR','VIAX','VIBK' ,'VIBY']
tk=[1,2,3,4,5]
ld=[1,2,3,4,5]
tx=[1,2,3,4,5]
rw=[1,2,3,4]
ps=[1,2,3,4,5,6,7,8]
@airport_blueprints.route('/add',methods=['GET','POST'])
def add():
	form=AddForm()
	print("hello")
	if request.method == "POST":
		print("validate")
		for i in range(len(icaos)):
			print("hello")
			icao=icaos[i]
			tk=np.random.randint(1,6)
			ld=np.random.randint(1,6)
			tx=np.random.randint(1,6)
			rw=np.random.randint(1,5)
			ps=np.random.randint(1,9)
			new_airport=Airport(icao,tx,ld,tx,rw,ps)
			db.session.add(new_airport)
			db.session.commit()
		return redirect(url_for('airport.airports_list'))	
	return render_template('airports_add.html',form=form)

@airport_blueprints.route('/airports_list')
def airports_list():
	airports= Airport.query.all()
	return render_template('airports_list.html',airports=airports)

@airport_blueprints.route('/planes',methods=['GET','POST'])
def planes():
	form=SelectForm()
	icaos=['abc',"VIAG", 'VIAM','VIAR','VIAX','VIBK' ,'VIBY']
	st=['abc','On ground','On Air']
	if form.validate_on_submit():
		city=form.city.data
		cy=icaos[int(city)]
		name=int(form.name.data)
		if name==1:
			data=db.session.query(Aircraft).filter(Aircraft.sc==cy).filter(Aircraft.altitude==0).all() 
		else:
			data=db.session.query(Aircraft).filter(Aircraft.sc==cy).filter(Aircraft.altitude>0).all() 
		
		print(data)
		if data==[]:
			data=['No data available']   
		return render_template('details.html',data=data)
	return render_template('gd.html',form=form)








