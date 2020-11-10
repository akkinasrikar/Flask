from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,SelectField


class AddForm(FlaskForm):
	submit = SubmitField("Get Data")

class SelectForm(FlaskForm):
	city= SelectField('airport',choices=[('1','VIAG'),('2','VIAM'),
		                                ('3','VIAR'),('4','VIAX'),('5','VIBK'),('6','VIBY')])
	name=SelectField('position',choices=[('1','On ground'),
		                                ('2','On Air')])
	submit=SubmitField("Get info")