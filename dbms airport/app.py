from myproject import app,db
from flask import render_template
from flask import render_template,request,redirect,url_for,flash,abort
from flask_login import login_user,logout_user,login_required
from myproject.forms import LoginForm,RegistrationForm
from myproject.models import User


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome():
	return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash("you logged out successfully")
	return redirect(url_for('home'))

@app.route('/login',methods=['GET', 'POST'])
def login():

	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user.check_password(form.password.data) and user is not None:

			login_user(user)
			flash("you logged in successfully")

			next=request.args.get('next')
			if next==None or not next[0]=='/':
				next=url_for('welcome')
			return redirect(next)
	return render_template('login.html',form=form)


@app.route('/register',methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		user=User(email=form.email.data, 
			username=form.username.data,
			password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("thanks for registration")
		return redirect(url_for('login'))
	return render_template('register.html',form=form)

if __name__ == '__main__':
	app.run(debug=True)