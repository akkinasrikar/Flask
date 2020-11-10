from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,SelectField


class AddForm(FlaskForm):

	name=StringField("name of Company")
	id=IntegerField("Id of the Pilot")
	submit = SubmitField("Add Company")

class SelectForm(FlaskForm):
	name=SelectField('company',choices=[('1','emrites'),
		                                ('2','airbus'),
		                                ('3','airindia'),
		                                ('4','qatar')])
	submit=SubmitField("Get info")