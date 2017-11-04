import json

class User:
	"""Class containing information about the user.
	
	Attributes:
	username: String that represents the username
	password: String that represents the password
	is_valid: Boolean that is true when the password is correct for given username
	"""

	def __init__(self, username, password):
		json_data=open("dummy_user.json").read()
		data = json.loads(json_data)
		if data[username]["password"] == password:
			self.username = username
			self.first_name = data[username]["first_name"]
			self.second_name = data[username]["second_name"]
			self.picture = data[username]["picture"]
			self.age = data[username]["age"]
			self.education = data[username]["education"]
			self.geography = data[username]["geography"]
			self.subreddit = data[username]["subreddit"]
			self.meme = data[username]["meme"]
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
			self.meme = ""
			self.is_valid = False

	def __str__(self):
		return "Username = " + self.username + "\nFirst Name = " + self.first_name + "\nSecond Name = " + self.second_name + "\nPicturelink = " + self.picture + "\nAge = " + self.age + "\nEducation = " + self.education + "\nGeography = " + self.geography + "\nSubreddit = " + self.subreddit + "\nMeme = " + self.meme

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