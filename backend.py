from flask import Flask, render_template

app = Flask(__name__)


class BackEnd:
	def __init__(self):
		return
		
	def displayText(self, message):
		# User inputs string parameter which is 
		# displayed on the webpage
		return message
	
	def displayImage(self, imageLink):
		# User inputs the image Link which is 
		# displayed on the webpage
		# WIP
		return imageLink

# creates instance of the class BackEnd file
test = BackEnd()

@app.route('/')
def index():
	return test.displayText("asdfasdf")

if __name__ == '__main__':
	app.run()
