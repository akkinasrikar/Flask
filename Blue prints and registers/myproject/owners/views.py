from flask import Blueprint,render_template,url_for,redirect
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprints=Blueprint('owners',__name__,template_folder='templates/owners')

@owners_blueprints.route('/add',methods=['GET', 'POST'])
def add():
	form=AddForm()
	if form.validate_on_submit():
		name=form.name.data
		id=form.id.data
		new_owner=Owner(name,id)
		db.session.add(new_owner)
		db.session.commit()
		return redirect(url_for('puppies.list'))	
	return render_template('add_owner.html',form=form)


