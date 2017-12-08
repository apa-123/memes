import json
from reddit import Reddit

class User:
	"""A User object containing information about the user.
	
	Attributes:
	username: A string representing the username
	first_name: A string representing the first name of the user
	second_name: A string representing the last name of the user
	bio: A string representing the biography of the user
	picture: A string representing a link to the picture of the user's profile pic
	age: A int representing the age of the user
	geography: A string representing the location of the user
	subreddit: A list representing the subreddits that the user is subscribed to
	"""

	def __init__(self, username):
		""" Return a User object whose username is *username*. The first name, last
		name, biography, picture, age, geography, and subreddit is taken
		from the database.
		"""
		data = Users.query.all()
		for u in data:
			print(u.username)
			if u.username == username:
				self.username = u.username
				self.first_name = u.first_name
				self.second_name = u.second_name
				self.bio = u.bio
				self.picture = u.picture
				self.age = u.age
				self.education = u.education
				self.geography = u.geography
				self.subreddit = u.subreddit
				self.is_valid_user = True
				return
		self.username = "Invalid User"
		self.first_name = "Invalid User"
		self.second_name = "Invalid User"
		self.picture = "Invalid User"
		self.age = "Invalid User"
		self.education = "Invalid User"
		self.geography = "Invalid User"
		self.subreddit = "Invalid User"
		self.meme = "Invalid User"
		self.is_valid_user = False



	def __str__(self):
		"""Prints out all the information about the user."""
		return "Username = " + self.username + "\nFirst Name = " \
			+ self.first_name + "\nSecond Name = " + self.second_name \
			+ "\nPicturelink = " + self.picture + "\nAge = " + self.age \
			+  "\nGeography = " + self.geography + "\nSubreddit = " \
			+ str(self.subreddit)

	def returnFirstName(self):
		"""Returns a string representing the first name of the user."""
		return self.first_name

	def returnSecondName(self):
		"""Returns a string representing the last name of the user."""
		return self.second_name


	def returnBio(self):
		"""Returns a string representing the biography of the user."""
		return self.bio


	def returnPicture(self):
		"""Returns a string representing the link of the user's profile picture"""
		return self.picture


	def returnAge(self):
		"""Returns a int representing the age of the user."""
		return self.age


	def returnGeography(self):
		"""Returns a string representing the location of the user."""
		return self.geography


	def returnSubreddit(self):
		"""Returns a list representing a list of subreddits that the user
		is subscribed to."""
		return self.subreddit

class PublicUser:
	"""Class containing information about the user.
	
	Attributes:
	username: ng that represents the username
	is_valid_user: Boolean that is true when the username exists
	"""
	def __init__(self, username):
		data = Users.query.all()
		#if username in data:
		for u in data:
			if u.username == username:
				self.username = u.username
				self.first_name = u.first_name
				self.second_name = u.second_name
				self.bio = u.bio
				self.picture = u.picture
				self.age = u.age
				self.education = u.education
				self.geography = u.geography
				self.subreddit = u.subreddit
				self.is_valid_user = True
			#self.username = username
			#self.first_name = data["accounts"][username]["first_name"]
			#self.second_name = data["accounts"][username]["second_name"]
			#self.bio = data["accounts"][username]["bio"]
			#self.picture = data["accounts"][username]["picture"]
			#self.age = data["accounts"][username]["age"]
			#self.education = data["accounts"][username]["education"]
			#self.geography = data["accounts"][username]["geography"]
			#self.subreddit = data["accounts"][username]["subreddit"]
			#self.meme = data["accounts"][username]["meme"]
			#self.is_valid_user = True
		self.username = "Invalid User"
		self.first_name = "Invalid User"
		self.second_name = "Invalid User"
		self.picture = "Invalid User"
		self.age = "Invalid User"
		self.education = "Invalid User"
		self.geography = "Invalid User"
		self.subreddit = "Invalid User"
		self.meme = "Invalid User"
		self.is_valid_user = False

	def __str__(self):
		if self.is_valid_user:
			return "Username = " + self.username + "\nFirst Name = " \
				   + self.first_name + "\nSecond Name = " + self.second_name \
				   + "\nPicturelink = " + self.picture + "\nAge = " + self.age \
				   + "\nEducation = " + self.education + "\nGeography = " \
				   + self.geography  + "\nMeme = " + self.meme + "\nSubreddit = " + str(self.subreddit)
		else:
			return "Not Available"

	def returnTitle(self):
		if self.is_valid_user:
			return "username = " + self.username + "\ntitle = " + self.title

	def returnMeme(self):
		if self.is_valid_user:
			return "username = " + self.username + "\nImage = " + self.meme
		else:
			return "Not Available"

	def returnFirstName(self):
		if self.is_valid_user:
			return "username = " + self.username + "\nfirst name = " + self.first_name
		else:
			return "Not Available"

	def returnSecondName(self):
		if self.is_valid_user:
			return "username = " + self.username + "\nsecond name = " + self.second_name
		else:
			return "Not Available"

	def returnBio(self):
		if self.is_valid_user:
			return "username = " + self.username + "\nBiography: " + self.bio
		else:
			return "Not Available"

	def returnPicture(self):
		if self.is_valid_user:
			return "username = " + self.username + "\npicture = " + self.picture
		else:
			return "Not Available"

	def returnAge(self):
		if self.is_valid_user:
			return "username = " + self.username + "\nAge = " + self.age
		else:
			return "Not Available"

	def returnEducation(self):
		if self.is_valid_user:
			return "username = " + self.username + "\nEducation = " + self.education
		else:
			return "Not Available"

	def returnGeography(self):
		if self.is_valid_user:
			return "username = " + self.username + "\nGeography = " + self.geography
		else:
			return "Not Available"

	def returnSubreddit(self):
		if self.is_valid_user:
			return self.subreddit
		else:
			return "Not Available"

from backend import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    second_name = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.String(120), nullable=False)
    picture = db.Column(db.String(120))
    age = db.Column(db.Integer, nullable=False)
    education = db.Column(db.String(120))
    geography = db.Column(db.String(120))
    subreddit = db.Column(db.String(200))

    def __repr__(self):
        return '<User %r>' % self.username