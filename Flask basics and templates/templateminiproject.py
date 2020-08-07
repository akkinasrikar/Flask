from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('submission.html')

@app.route('/checking')
def check():
	name=request.args.get('name')
	letters=list(name)
	conditions=['Name must contain Lower case letter',
	            'Name must contain Upper case letter',
	            'Name must contain Number']
	a,b,c=0,1,2
	for i in letters:
		if 97<=ord(i)<=122:
			try:
				conditions.remove('Name must contain Lower case letter')
			except:
				pass
		elif 65<=ord(i)<=90:
			try:
				conditions.remove('Name must contain Upper case letter')
			except:
				pass
		elif 48<=ord(i)<=57:
			try:
				conditions.remove('Name must contain Number')
			except:
				pass
	return render_template('checking.html',name=name,conditions=conditions)


if __name__=='__main__':
	app.run(debug=True)