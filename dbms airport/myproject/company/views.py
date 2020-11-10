from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Company
from myproject.models import Pilot
from myproject.company.forms import AddForm,SelectForm


company_blueprints=Blueprint('company',__name__,template_folder='templates/company')

@company_blueprints.route('/add',methods=['GET', 'POST'])
def add():
	form=AddForm()
	if form.validate_on_submit():
		name=form.name.data
		id=form.id.data
		new_company=Company(name,id)
		db.session.add(new_company)
		db.session.commit()
		return redirect(url_for('pilots.list'))	
	return render_template('add_company.html',form=form)

@company_blueprints.route('/list')
def company_list():
	companies= Company.query.all()
	return render_template('company_list.html',companies=companies)

@company_blueprints.route('/cpno')
def cpno():
	companies= db.session.query(Company.name,db.func.count(Company.name)).group_by(Company.name).all()
	return render_template('cpno.html',companies=companies)

@company_blueprints.route('/ojpc')
def ojpc():
	data=db.session.query(Pilot.id,Pilot.first_name,Pilot.last_name,Pilot.age,Pilot.rank,Company.name).outerjoin(Company,Company.pilot_id==Pilot.id).all();   
	return render_template('ojpc.html',data=data)

@company_blueprints.route('/info',methods=['GET','POST'])
def info():
	form=SelectForm()
	l=['abc','emrites','airbus','airindia','qatar']
	if form.validate_on_submit():
		name=form.name.data
		comp=l[int(name)]
		data=db.session.query(Pilot.id,Pilot.first_name,Pilot.last_name,Pilot.age,Pilot.rank,Company.name).filter(Company.name==comp).outerjoin(Company,Company.pilot_id==Pilot.id).all();
		if data==[]:
			data=['No data available']   
		print(data)
		return render_template('get_details.html',data=data)
	return render_template('info.html',form=form)


