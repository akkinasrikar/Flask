from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Pilot
from myproject.pilots.forms import AddForm,DelForm

pilots_blueprints=Blueprint('pilots',__name__,template_folder='templates/pilots')

@pilots_blueprints.route('/add',methods=['GET', 'POST'])
def add():
	form=AddForm()
	if form.validate_on_submit():
		first_name=form.first_name.data
		last_name=form.last_name.data
		age=form.age.data
		rank=form.rank.data
		new_pilot=Pilot(first_name,last_name,age,rank)
		db.session.add(new_pilot)
		db.session.commit()
		return redirect(url_for('pilots.list'))	
	return render_template('add.html',form=form)

@pilots_blueprints.route('/list')
def list():
	pilots= Pilot.query.all()
	return render_template('list.html',pilots=pilots)

@pilots_blueprints.route('/delete',methods=["get","post"])
def delete():
	form = DelForm()
    
	if form.validate_on_submit():

		id=form.id.data
		pilot= Pilot.query.get(id)
		db.session.delete(pilot)
		db.session.commit()
		return redirect(url_for('pilots.list'))
	return render_template('delete.html', form=form)

@pilots_blueprints.route('/exp')
def exp():
	pilots =db.session.query(Pilot.first_name,Pilot.age).order_by(Pilot.age.desc()).all()
	return render_template('exp.html', pilots=pilots)