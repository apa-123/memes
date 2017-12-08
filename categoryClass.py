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
        json_data = open("dummy_user.json").read()
        data = json.loads(json_data)
        if username in data["categories"]:
            self.username = username
            self.picture = data["categories"][username]["picture"]
            self.subreddit = data["categories"][username]["subreddit"]
            self.bio = data["categories"][username]["bio"]
            self.is_valid_cat = True

        else:
            self.username = "Invalid Category"
            self.picture = "Invalid Category"
            self.subreddit = "Invalid Category"
            self.bio = "Invalid Category"
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
    bio = db.Column(db.String(120), nullable=False)
    picture = db.Column(db.String(120))
    subreddit = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.username