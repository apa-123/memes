# memes 
##
Group Members - Aparajitha Adiraju, Bryan Cheng, Aditya Bhansali, Rena Xu, Thomas Yang

## What is it:
A social media web application where users can create personalized profiles to post and follow memes.

## Technologies used:
- SQLAlchemy Database used for the backend
- Python Flask used to connect backend and frontend
- HTML/CSS/Bootstrap used to code the user interface 
- Reddit API used to obtain the memes

## Future improvements:
- Deploy to AWS so it is not on a local host
- Add more user functionality (the ability to follow other users and post)
- Improve the UI to make it easier to navigate 
- Complete the Unittests

## Flask Information:

What is Flask? Webdev framework to manage HTML/CSS -- work with databases

###### To code a simple application
- Import Flask 
- Create instance
- Route to a url
** don’t name your function flask (conflicts) 

###### Example Program:
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
   ```
###### To run your Flask app
```
$ export FLASK_APP=hello.py -- set on Windows 
$ flask run		
```
* Running on http://127.0.0.1:5000/

###### To debug your Flask app
```
$ export FLASK_DEBUG=1 
$ flask run
```

###### Routing
The route() decorator is used to bind a function to a URL
```
@app.route('/') 
def index(): 
    return 'Index Page'

@app.route('/hello')
def hello():
    return ‘Hello, World’
```

###### Helpful Links
- http://flask.pocoo.org/docs/0.12/.latex/Flask.pdf
- https://github.com/pallets/flask/tree/master/examples/minitwit/
- https://conda.io/docs/user-guide/install/linux.html

## Extra Information:

Windows - creating virtual environment
	conda create -n virtualenv
	activate virtualenv

Deactivate active environment
	deactivate 
	
Externally Visible Server: If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line
flask run --host=0.0.0.0 (tell the operating system to listen to all IPs)
					
What to do if the Server does not Start: if the module is incorrectly named, will get import error. It will tell you what it tried to import any why failed. Most common reason is a typo (did not create an app object)

###### Unique URLs/Redirection Behavior: 
```
@app.route(‘/projects/’)
def projects():
    return ‘The project page’

@app.route(‘/about’)
def about():
    return ‘The about page’
```
Differ in the use of trailing slash. Access the first one without trailing slash redirect to the canonical URL with slash. Access the second one with trailing slash will create 404 “Not Found” error.
				
			
## HTML Information:

- Import render_template
- Create folder with templates
- Create html file
- In the defined function return render_template(‘home.html’)
	The contents of home.html will be what is displayed onto the server

Can create a layout.html to simplify the html files-

In the <body> of the layout.html, include
```
	{% block body %}{% endblock %}
```
Then in the .html file add
```
	{% extends ‘layout.html’ %}
	{% block body %}
	{% endblock %}
```
This makes it so that the .html file will have the layout of layout.html
Any text put in between block body and endblock will basically be text put in between <body> and </body>

###### Example layout.html file: 
```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>MyFlaskApp</title>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	</head>
	<body>
		{% block body %}{% endblock %}

		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	</body>
</html
```

## Reddit API Information:

###### Helpful links:
- https://www.reddit.com/dev/api 
- http://docs.python-requests.org/en/latest/
- http://www.pythonforbeginners.com/api/how-to-use-reddit-api-in-python

###### Example Code: 
```
import json
import requests

r = requests.get(
    'https://reddit.com/r/all.json',
    headers={'User-Agent': ''}
)
r.text # Unformatted text

reddit_json = json.loads(r.text)
reddit_json
```

