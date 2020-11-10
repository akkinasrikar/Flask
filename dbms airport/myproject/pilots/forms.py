from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

	first_name = StringField("First Name: ")
	last_name = StringField("Last Name: ")
	age = IntegerField("Age: ")
	rank = IntegerField("Rank: ")
	submit = SubmitField("Register")

class DelForm(FlaskForm):

	id=IntegerField("ID number of Pilot")
	submit = SubmitField("remove pilot")