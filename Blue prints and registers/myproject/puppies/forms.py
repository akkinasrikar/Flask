from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

	name = StringField("name of puppy")
	submit = SubmitField("add puppy")

class DelForm(FlaskForm):

	id=IntegerField("id number of puppy to remove")
	submit = SubmitField("remove puppy")