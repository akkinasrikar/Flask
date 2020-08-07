from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def home():
	return render_template('templateinherictence(home).html')

@app.route('/puppy/<name>')
def puppy(name):
	return render_template('puppy.html',name=name)


@app.route('/flow')
def controloverflow():
	mylist=[1,2,3,4,5]
	return render_template('templatecontrolflow.html',mylist=mylist)


@app.route('/basic')
def index():
	name="hermoine"
	magic={'black spell':'harry',
	       'blue spell':'hermoine'}
	return render_template('basic.html',my_variable=name,magic=magic)

if __name__=='__main__':
	app.run(debug=True)