from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class AddForm(FlaskForm):

	name=StringField("name of owner")
	id=IntegerField("Id of the puppy")
	submit = SubmitField("Add owner")