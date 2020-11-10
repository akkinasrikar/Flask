from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Aircraft
from flask import request
from myproject.aircraft.forms import AddForm,SelectForm,SpeedForm
import pandas as pd
import numpy as np

aircraft_blueprints=Blueprint('aircraft',__name__,template_folder='templates/aircraft')

data=pd.read_csv("C:\\Users\\personal\\Desktop\\dbms final\\dbms airport\\myproject\\aircraft\\airplane.csv")
print(data.head())
comps=['airbus','emrites','qatar','airindia']
places=['VIAG', 'VIAM','VIAR','VIAX','VIBK' ,'VIBY']
l=100
@aircraft_blueprints.route('/add',methods=['GET','POST'])
def add():
	form=AddForm()
	print("hello")
	if request.method == "POST":
		print("validate")
		no=form.no.data
		print(no)
		for i in range(no):
			print("hello")
			call_sign="aircraft"+str(i)
			model_no=data['model_no'][i]
			turn_around_count=np.random.randint(1,5)
			a=np.random.randint(0,5)
			sc=places[a]
			ds=places[a+1]
			emergency=np.random.randint(0,2)
			b=np.random.randint(0,2)
			if b==0:
				altitude=0
			else:
				altitude=np.random.randint(100,21000)
			pilot=np.random.randint(1,10)
			distance=np.random.randint(100,1000)
			crash=np.random.randint(0,2)
			company=data['model_no'][i].split()[0]
			speed=np.random.randint(100,1000)
			delay=np.random.randint(0,100)
			new_aircraft=Aircraft(call_sign,model_no,turn_around_count,sc,ds,emergency,
				                  altitude,pilot,distance,crash,company,speed,delay)
			print(f"aircraft:{i}")
			db.session.add(new_aircraft)
			db.session.commit()
		return redirect(url_for('aircraft.aircrafts_list'))	
	return render_template('aircrafts_add.html',form=form)

@aircraft_blueprints.route('/aircrafts_list')
def aircrafts_list():
	aircrafts= Aircraft.query.all()
	return render_template('aircrafts_list.html',aircrafts=aircrafts)

@aircraft_blueprints.route('/aircrafts_det',methods=['GET','POST'])
def aircrafts_det():
	form=SelectForm()
	icaos=['abc',"VIAG", 'VIAM','VIAR','VIAX','VIBK' ,'VIBY']
	if form.validate_on_submit():
		sc=icaos[int(form.sc.data)]
		ds=icaos[int(form.ds.data)]
		print(sc,ds)
		if sc==ds:
			data=[["go back and select different source and destination"]]
		else:
			data=db.session.query(Aircraft.call_sign,Aircraft.model_no,Aircraft.sc,Aircraft.ds).filter(Aircraft.sc==sc).filter(Aircraft.ds==ds).all()
		if data==[]:
			data=['No data available']
		return render_template('infod.html',data=data)
	return render_template('dt.html',form=form)

@aircraft_blueprints.route('/aircrafts_speed',methods=['GET','POST'])
def aircrafts_speed():
	form=SpeedForm()
	sp=['abc',100,300,500,700,800 ,900]
	if form.validate_on_submit():
		s=sp[int(form.s.data)]
		data=db.session.query(Aircraft).filter(Aircraft.speed>s).all() 
		if data==[]:
			data=['No data available']
		return render_template('speeddata.html',data=data)
	return render_template('st.html',form=form)










