from flask import Flask

app = Flask(__name__)

class BackEnd:
	def __init__(self):
		
	def displayText(self, message):
		return message
	
	def displayImage(self, imageLink):
		return imageLink
@app.route('/')
def index():
	return "asdf"

if __name__ == '__main__':
	app.run()
