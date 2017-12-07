from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from reddit import Reddit
from memecl import Memes
from userClass import User
from categoryClass import Category

'''
This class uses the User, PublicUser, Meme and Category classes 
to render the user and category pages.

This is done using a Flask app. Read more about Flask here:
http://flask.pocoo.org/

'''

app = Flask('Memes')

# Number of posts to render
NUM_POSTS = 10

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

    return render_template('login_page.html')

@app.route('/signup')
def create_user_page():
    '''
    Renders the create User page.

    @return: html of create user page
    '''

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
