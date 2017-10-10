from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def homePage():
    return "<h1>Test Index Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)