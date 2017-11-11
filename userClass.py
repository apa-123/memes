import json
from reddit import Reddit

class User:



	"""Class containing information about the user.
	
	Attributes:
	username: ng that represents the username
	password: ng that represents the password
	is_valid: Boolean that is true when the password is correct for given username
	"""

	def __init__(self, username, password):
		json_data=open("dummy_user.json").read()
		data = json.loads(json_data)
		if username in data["accounts"]:			
			if data["accounts"][username]["password"] == password:
				self.username = username
				self.first_name = data["accounts"][username]["first_name"]
				self.second_name = data["accounts"][username]["second_name"]
				self.picture = data["accounts"][username]["picture"]
				self.age = data["accounts"][username]["age"]
				self.education = data["accounts"][username]["education"]
				self.geography = data["accounts"][username]["geography"]
				self.subreddit = data["accounts"][username]["subreddit"]
				self.is_valid = True
			else:
				self.username = username
				self.first_name = ""
				self.second_name = ""
				self.picture = ""
				self.age = ""
				self.education = ""
				self.geography = ""
				self.subreddit = ""
				self.is_valid = False
		else:
			self.username = "Invalid User"
			self.first_name = "Invalid User"
			self.second_name = "Invalid User"
			self.picture = "Invalid User"
			self.age = "Invalid User"
			self.education = "Invalid User"
			self.geography = "Invalid User"
			self.subreddit = "Invalid User"
			self.is_valid = False

	def __str__(self):
		return "Username = " + self.username + "\nFirst Name = " \
		+ self.first_name + "\nSecond Name = " + self.second_name \
		+ "\nPicturelink = " + self.picture + "\nAge = " + self.age \
		+ "\nEducation = " + self.education + "\nGeography = " \
		+ self.geography + "\nSubreddit = " + str(self.subreddit)

	def returnFirstName(self):
		return "username = " + self.username + "\nfirst name = " + self.first_name

	def returnSecondName(self):
		return "username = " + self.username + "\nsecond name = " + self.second_name

	def returnPicture(self):
		return "username = " + self.username + "\npicture = " + self.picture

	def returnAge(self):
		return "username = " + self.username + "\nAge = " + self.age

	def returnEducation(self):
		return "username = " + self.username + "\nEducation = " + self.education

	def returnGeography(self):
		return "username = " + self.username + "\nGeography = " + self.geography

	def returnSubreddit(self):
		return "username = " + self.username + "\nSubreddit = " + self.subreddit

	def returnMeme(self):
		return "username = " + self.username + "\nMeme = " + self.meme


