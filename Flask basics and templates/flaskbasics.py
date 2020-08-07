from flask import Flask

app=Flask(__name__)

@app.route('/')

def index():
	return "<h1>Hello puppy</h1>"

@app.route('/information')
def info():
	return "<h1>puppies are cute</h1> "

@app.route('/puppy/<name>')
def puppy(name):
	return "<h1>Hello {}</h1>".format(name)

@app.route('/info/<word>')
def uppercase(word):
	return f"upper case : {word.upper()}"

@app.route('/debugger/<name>')
def debugging(name):
	return f"100 th letter is {name[100]}"


if __name__=='__main__':
	app.run(debug=True)