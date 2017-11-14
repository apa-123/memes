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

numPosts = 3

# intitialize category
def initCategory(name):
	return Category(name)

def initUser(name):
	return PublicUser(name)

# get category information:
def getCategory(cat):
	reddit = Reddit(cat.subreddit[0], numPosts)
	urls = reddit.getImageUrl()
	titles = reddit.getTitle()
	scores = reddit.getScore()
	authors = reddit.getAuthor()
	return [urls, titles, scores, authors]

def getUser(user):
	print(str(user.returnSubreddit()))
	reddit = Reddit(user.returnSubreddit()[2], numPosts)
	urls = reddit.getImageUrl()
	titles = reddit.getTitle()
	scores = reddit.getScore()
	authors = reddit.getAuthor()
	return [urls, titles, scores, authors]


# home page
@app.route('/')
def index():
	return render_template('index.html')

# user home page
@app.route('/users')
def user():
	name = request.args.get('user')
	user = initUser(name)
	[urls, titles, scores, authors] = getUser(user)
	return render_template('category_page.html', name=name, img_1_url=urls[0], img_2_url=urls[1], img_3_url=urls[2], source_img="content/reddit_logo.png")

@app.route('/category')
def category():
	name = request.args.get('cat')
	print("Getting category " + name)
	category = initCategory(name)
	print("Getting data")
	[urls, titles, scores, authors] = getCategory(category)
	return render_template('category_page.html', name=name, img_1_url=urls[0], img_2_url=urls[1], img_3_url=urls[2], source_img="content/reddit_logo.png")

if __name__ == '__main__':
	app.run(debug=True)
