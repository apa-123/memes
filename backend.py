from flask import Flask
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)

# helper functions	
def displayText(message):
	# User inputs string parameter which is 
	# displayed on the webpage
	return message
	
def displayImage(name):
	# User inputs the image Link which is 
	# displayed on the webpage
	return render_template('home.html', name=name)

# home page
@app.route('/')
def index():
	return render_template('index.html')

# user home page
@app.route('/users')
def user():
	name = request.args.get('user')
	return render_template('user_page.html', name=name)

@app.route('/category')
def category():
	name = request.args.get('user')
	return render_template('user_page.html', name=name)

if __name__ == '__main__':
	app.run()
