import json
from pprint import pprint

class User:

	def __init__(self, username):
		json_data=open("dummy_user.json").read()
		data = json.loads(json_data)

		self.username = username
		self.first_name = data[username]["first_name"]
		self.second_name = data[username]["second_name"]
		self.picture = data[username]["picture"]
		self.age = data[username]["age"]
		self.education = data[username]["education"]
		self.geography = data[username]["geography"]
		self.subreddit = data[username]["subreddit"]
		self.meme = data[username]["meme"]

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