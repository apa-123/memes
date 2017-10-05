# memes

Useful Links
http://flask.pocoo.org/docs/0.12/.latex/Flask.pdf
https://github.com/pallets/flask/tree/master/examples/minitwit/
https://conda.io/docs/user-guide/install/linux.html

Webdev framework to manage HTML/CSS -- work with databases

To code a simple application
Import Flask 
Create instance
Route to a url
** don’t name your function flask. -- conflicts 

To run your Flask app
	$ export FLASK_APP=hello.py -- set on Windows 
	$ flask run						
	* Running on http://127.0.0.1:5000/


To debug your Flask app
	$ export FLASK_DEBUG=1 
	$ flask run


Routing
The route() decorator is used to bind a function to a URL
	@app.route('/') 
	def index(): 
	    return 'Index Page'

	@app.route('/hello')
	def hello():
	    return ‘Hello, World’


Example program
	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
	    return "Hello World!"


Windows - creating virtual environment
	conda create -n virtualenv
	activate virtualenv

Deactivate active environment
	deactivate 

External things we learned: how to install conda, which can be used to download most files 


Externally Visible Server: If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line
----flask run --host=0.0.0.0 (tell the operating system to listen to all IPs)
		
					
What to do if the Server does not Start: if the module is incorrectly named, will get import error. It will tell you what it tried to import any why failed. Most common reason is a typo (did not create an app object)


Unique URLs/Redirection Behavior: 
	@app.route(‘/projects/’)
	def projects():
	    return ‘The project page’

	@app.route(‘/about’)
	def about():
	    return ‘The about page’
Differ in the use of trailing slash. Access the first one without trailing slash redirect to the canonical URL with slash. Access the second one with trailing slash will create 404 “Not Found” error.
				
			
		


