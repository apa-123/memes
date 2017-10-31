from flask import Flask, render_template

app = Flask(__name__)

# helper functions	
def displayText(message):
	# User inputs string parameter which is 
	# displayed on the webpage
	return message
	
def displayImage(name):
	# User inputs the image Link which is 
	# displayed on the webpage
	# WIP
	return render_template('home.html', name=name)

# home page
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
