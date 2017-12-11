import os
from flask import Flask, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from reddit import Reddit
from memecl import Memes
from registration_form import *
'''
This class uses the User, 
, Meme and Category classes 
to render the user and category pages.

This is done using a Flask app. Read more about Flask here:
http://flask.pocoo.org/

'''

app = Flask('Memes')

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    second_name = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.String(120))
    picture = db.Column(db.String(120))
    age = db.Column(db.Integer)
    education = db.Column(db.String(120))
    geography = db.Column(db.String(120))
    subreddit = db.Column(db.String(200))

    def __repr__(self):
        return '<User %r>' % self.username
db.create_all()
db.session.commit()

# Number of posts to render

def createUser(username, password, first_name, second_name):
    user = Users(username = username, password = password, first_name = first_name, second_name = second_name, bio = None, picture = None, age = None, education = None, geography = None, subreddit = None)
    db.session.add(user)
    db.session.commit()

NUM_POSTS = 5

def init_category(name):
    '''
    Creates a new category object which points to the category with
    the specified name.

    @param: the name of the category
    @return: Category object pointing to given category
    '''
    return Category(name)

def init_user(name):
    '''
    Creates a new public user object which points to the user with
    the specified name.

    @param: the name of the user
    @return: PublicUser object pointing to a given user 
    '''
    return User(name)

def get_category(category):
    '''
    Gets the information from the specified public category object.

    @param: Category object representing the target category
    @return: a 2D parallel list: [img_urls, titles, scores, authors]
    '''
    
    # initializes the reddit praw wrapper
    reddit = Reddit(category.subreddit[0], NUM_POSTS)

    # gets the data from reddit
    img_urls = reddit.getImageUrl()
    titles = reddit.getTitle()
    scores = reddit.getScore()
    authors = reddit.getAuthor()

    return [img_urls, titles, scores, authors]

def get_user(user):
    '''
    Gets the information from the specified public user object.

    @param: the PublicUser object that points to the target user
    @return: a 2D parallel list: [img_urls, titles, scores, authors]
    '''
    # initializes the reddit praw wrapper
    reddit = Reddit(user.returnSubreddit()[2], NUM_POSTS)

    # gets the data from reddit
    img_urls = reddit.getImageUrl()
    titles = reddit.getTitle()
    scores = reddit.getScore()
    authors = reddit.getAuthor()

    return [img_urls, titles, scores, authors]

@app.route('/')
def index():
    '''
    Renders the index page.

    @return: html of index page
    '''
    return render_template('index.html')

# user home page
@app.route('/users')

def user():
	name = request.args.get('user')
	user = User(name)
	[urls, titles, scores, authors] = get_user(user)
	return render_template('category_page.html',name=name, img_1_url=urls[0], img_2_url=urls[1], img_3_url=urls[2], source_img="content/reddit_logo.png")

def public_user_page():
    '''
    Renders the user page.

    @return: html of index page with image URLs
    '''

    # Gets the target category from the URL
    name = request.args.get('user')

    # Initializes the PublicUser object
    user = init_user(name)
    
    # Gets the data from the API
    [img_urls, titles, scores, authors] = get_user(user)

    return render_template('category_page.html', name=name,
    img_1_url=img_urls[0], img_2_url=img_urls[1], img_3_url=img_urls[2],
    source_img="content/reddit_logo.png")


@app.route('/category')
def category_page():
    '''
    Renders the category page.

    @return: html of cateogry page with image URLs
    '''

    # Gets the target category from the URL
    name = request.args.get('cat')

    # Initializes the PublicUser object
    category = init_category(name)
    
    # Gets the data from the API
    [img_urls, titles, scores, authors] = get_category(category)

    return render_template('category_page.html', numPost=range(NUM_POSTS), name=name, 
        img_urls=img_urls, titles=titles, scores=scores, authors=authors,
        source_img="static/content/reddit_logo.png")

@app.route('/login')
def login_page():
    '''
    Renders the login page.

    @return: html of login page
    '''

    return render_template('loginPage.html')
@app.route('/login/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        first = request.form['fname']
        last = request.form['lname']
        usernamess = request.form['username']
        usernames = db.session.query(Users.username)
        for x in usernames:
            if(usernamess in x):
                return render_template('form.html')
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        createUser(usernamess,password,first,last)
        # flash("No bueno")
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from userClass import *
from categoryClass import *
