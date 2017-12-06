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
            self.is_valid_cat = ""
    """ 
    Overloading of str class is used to return all attributes of a category in a string (like the toString method)
    """
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


