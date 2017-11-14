import json
from reddit import Reddit

class User:
	"""Class containing information about the user.
	
	Attributes:
	username: ng that represents the username
	password: ng that represents the password
	is_valid_user: Boolean that is true when the username exists
	is_valid_pass: Boolean that is true when password is correct for username
	"""

	def __init__(self, username, password):
		json_data=open("dummy_user.json").read()
		data = json.loads(json_data)
		if username in data["accounts"]:			
			if data["accounts"][username]["password"] == password:
				self.username = username
				self.first_name = data["accounts"][username]["first_name"]
				self.second_name = data["accounts"][username]["second_name"]
				self.bio = data["accounts"][username]["bio"]
				self.picture = data["accounts"][username]["picture"]
				self.age = data["accounts"][username]["age"]
				self.education = data["accounts"][username]["education"]
				self.geography = data["accounts"][username]["geography"]
				self.subreddit = data["accounts"][username]["subreddit"]
				self.is_valid_user = True
				self.is_valid_pass = True
			else:
				self.username = username
				self.first_name = ""
				self.second_name = ""
				self.picture = ""
				self.age = ""
				self.education = ""
				self.geography = ""
				self.subreddit = ""
				self.is_valid_user = True
				self.is_valid_pass = False
		else:
			self.username = "Invalid User"
			self.first_name = "Invalid User"
			self.second_name = "Invalid User"
			self.picture = "Invalid User"
			self.age = "Invalid User"
			self.education = "Invalid User"
			self.geography = "Invalid User"
			self.subreddit = "Invalid User"
			self.is_valid_user = False
			self.is_valid_pass = False

	def __str__(self):
		if self.is_valid_user:
			return "Username = " + self.username + "\nFirst Name = " \
				+ self.first_name + "\nSecond Name = " + self.second_name \
				+ "\nPicturelink = " + self.picture + "\nAge = " + self.age \
				+ "\nEducation = " + self.education + "\nGeography = " \
				+ self.geography + "\nSubreddit = " + str(self.subreddit)
		else:
			return "Not Available"

	def returnFirstName(self):
		if self.is_valid_user and self.is_valid_pass:
			return "username = " + self.username + "\nfirst name = " + self.first_name
		else:
			return "Not Available"

	def returnSecondName(self):
		if self.is_valid_user and self.is_valid_pass:
			return "username = " + self.username + "\nsecond name = " + self.second_name
		else:
			return "Not Available"

	def returnBio(self):
		if self.is_valid_user and self.is_valid_pass:
			return "username = " + self.username + "\nBiography: " + self.bio
		else:
			return "Not Available"

	def returnPicture(self):
		if self.is_valid_user and self.is_valid_pass:
			return "username = " + self.username + "\npicture = " + self.picture
		else:
			return "Not Available"

	def returnAge(self):
		if self.is_valid_user and self.is_valid_pass:
			return "username = " + self.username + "\nAge = " + self.age
		else:
			return "Not Available"

	def returnEducation(self):
		if self.is_valid_user and self.is_valid_pass:
			return "username = " + self.username + "\nEducation = " + self.education
		else:
			return "Not Available"

	def returnGeography(self):
		if self.is_valid_user and self.is_valid_pass:
			return "username = " + self.username + "\nGeography = " + self.geography
		else:
			return "Not Available"

	def returnSubreddit(self):
		if self.is_valid_user and self.is_valid_pass:
			return self.subreddit
		else:
			return "Not Available"

class PublicUser:
	"""Class containing information about the user.
	
	Attributes:
	username: ng that represents the username
	is_valid_user: Boolean that is true when the username exists
	"""
	def __init__(self, username):
		json_data = open("dummy_user.json").read()
		data = json.loads(json_data)
		if username in data["accounts"]:
			self.username = username
			self.first_name = data["accounts"][username]["first_name"]
			self.second_name = data["accounts"][username]["second_name"]
			self.bio = data["accounts"][username]["bio"]
			self.picture = data["accounts"][username]["picture"]
			self.age = data["accounts"][username]["age"]
			self.education = data["accounts"][username]["education"]
			self.geography = data["accounts"][username]["geography"]
			self.subreddit = data["accounts"][username]["subreddit"]
			self.meme = data["accounts"][username]["meme"]
			self.is_valid_user = True
		else:
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
