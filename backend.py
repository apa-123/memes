from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from reddit import Reddit
from memecl import Memes
from userClass import User
from userClass import PublicUser
from categoryClass import Category

app = Flask(__name__)

# Number of posts to render
NUM_POSTS = 3

def init_category(name):
    '''
    Creates a new category object which points to the category with
    the specified name.
    '''
    return Category(name)

def init_public_user(name):
    '''
    Creates a new public user object which points to the user with
    the specified name.
    '''
    return PublicUser(name)

def get_category(category):
    '''
    Gets the information from the specified public category object.

    Returns a 2D parallel list: [img_urls, titles, scores, authors]
    '''
    
    # initializes the reddit praw wrapper
    reddit = Reddit(category.subreddit[0], NUM_POSTS)

    # gets the data from reddit
    img_urls = reddit.getImageUrl()
    titles = reddit.getTitle()
    scores = reddit.getScore()
    authors = reddit.getAuthor()

    return [img_urls, titles, scores, authors]

def get_public_user(user):
    '''
    Gets the information from the specified public user object.

    Returns a 2D parallel list: [img_urls, titles, scores, authors]
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
    '''
    return render_template('index.html')

# user home page
@app.route('/users')
def public_user_page():
    '''
    Renders the user page.
    '''

    name = request.args.get('user')
    user = init_public_user(name)

    [img_urls, titles, scores, authors] = get_public_user(user)

    return render_template('category_page.html', name=name,
    img_1_url=img_urls[0], img_2_url=img_urls[1], img_3_url=img_urls[2],
    source_img="content/reddit_logo.png")

@app.route('/category')
def category_page():
    '''
    Renders the category page.
    '''

    name = request.args.get('cat')
    category = init_category(name)
    
    [img_urls, titles, scores, authors] = get_category(category)
    
    return render_template('category_page.html', name=name,
    img_1_url=img_urls[0], img_2_url=img_urls[1], img_3_url=img_urls[2],
    source_img="content/reddit_logo.png")

if __name__ == '__main__':
    app.run(debug=True)
