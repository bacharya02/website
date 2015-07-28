from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/bikash')
def hello_bikash():
	a='Bikash can math ' 
	f='<p>'	
	b='2*4='
	c=2*4
	e=str(c)	
	d=a + f + b + e	
	return d

#if __name__=='__main__':
#	app.run()
