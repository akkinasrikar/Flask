from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,SelectField


class AddForm(FlaskForm):
	no = IntegerField("No of flights: ")
	submit = SubmitField("Get Data")

class SelectForm(FlaskForm):
	sc= SelectField('airport',choices=[('1','VIAG'),('2','VIAM'),('3','VIAR'),('4','VIAX'),('5','VIBK'),('6','VIBY')])
	ds=SelectField('airport',choices=[('1','VIAG'),('2','VIAM'),('3','VIAR'),('4','VIAX'),('5','VIBK'),('6','VIBY')])
	submit=SubmitField("Get info")

class SpeedForm(FlaskForm):
	s= SelectField('airport',choices=[('1','>100'),('2','>300'),('3','>500'),('4','>700'),('5','>800'),('6','>900')])
	submit=SubmitField("Get info")
