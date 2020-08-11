from flask import Flask,render_template,flash,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY']='srikar'

class SimpleForm(FlaskForm):
	submit=SubmitField("click me")
	breed=StringField("What is your breed")

@app.route('/',methods=['GET','POST'])
def index():
	form = SimpleForm()
	if form.validate_on_submit():
		Dogbreed=form.breed.data
		flash(f'just updated your breed {Dogbreed}')
		return redirect(url_for('index'))
	return render_template('alert.html',form=form)

if __name__ == '__main__':
	app.run(debug=True)