from flask import Flask

app = Flask(__name__)


class BackEnd:
	def __init__(self):
		return
		
	def displayText(self, message):
		return message
	
	def displayImage(self, imageLink):
		return imageLink


test = BackEnd()

@app.route('/')
def index():
	return test.displayText("asdfasdf")

if __name__ == '__main__':
	app.run()
