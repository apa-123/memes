import json
from reddit import Reddit


class Category:
    """Class containing information about the category.

    Attributes:
    username: ng that represents the username
    password: ng that represents the password
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

    def returnPicture(self):
        return "username = " + self.username + "\npicture = " + self.picture

    def returnSubreddit(self):
        return "username = " + self.username + "\nSubreddit = " + self.subreddit

    def returnBio(self):
        return "username = " + self.username + "\nBio = " + self.bio

from backend import db

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.String(1200), nullable=False)
    picture = db.Column(db.String(120))
    subreddit = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.username