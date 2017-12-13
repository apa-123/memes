import json
from reddit import Reddit


class Category:
    """
    Class containing information about the categories that exist. No password verification that exists  

    Attributes:
    self: always an attribute of the __init__ function
    username: name of the category that is passed through the init function
    is_valid_cat: Boolean that is true when the username for the category exists
    """

    def __init__(self, username):
        data = Categories.query.all()
        for u in data:
            if u.username == username:
                self.username = u.username
                self.bio = u.bio
                self.picture = u.picture
                self.subreddit = u.subreddit
                self.is_valid_cat = True
                return
        self.username = "Invalid User"
        self.bio = "Invalid User"
        self.picture = "Invalid User"
        self.subreddit = "Invalid User"
        self.is_valid_cat = False

    def __str__(self):
        return "Username = " + self.username + self.first_name + "\nSecond Name = " + self.second_name \
               + "\nPicturelink = " + self.picture + self.bio + "\nSubreddit = " + str(self.subreddit)
    """
    These functions allow individual attributes of each category to be access as they are returned
    """

    def get_picture(self):
        return "username = " + self.username + "\npicture = " + self.picture

    def get_subreddit(self):
        return "username = " + self.username + "\nSubreddit = " + self.subreddit

    def get_bio(self):
        return "username = " + self.username + "\nBio = " + self.bio

from backend import db

class Categories(db.Model):

    '''A Categories database.

	Attributes:
	username: A string representing the category
	bio: A string representing the biography of the Category
	picture: A string representing a link to the picture of the category pic
	subreddit: A list representing the subreddits 
	'''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.String(1200), nullable=False)
    picture = db.Column(db.String(120))
    subreddit = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.username