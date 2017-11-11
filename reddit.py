import praw 
from pprint import pprint

import requests

import json#reddit wrapper, helps parse json. Short for python reddit api wrapper. Must install it to run it.  

#following is trying to get reddit json. To get a short description of the subreddit, go to reddit.com/reddits. Then get the json of /reddits and parse it to find the "public description" and get the string afterward to get the short description. Haven't found any other way of finding short description. Haven't done so yet.
'''
#import requests
#r = requests.get(
    'https://reddit.com/reddits.json',
    headers={'User-Agent': ''}
)
r.text # Unformatted text
reddit_json = json.loads(r.text)
reddit_json
'''
class Reddit:

	def __init__(self, nameOfSubreddit, limits):
		self.nameOfSubreddit = nameOfSubreddit
		self.limits = limits
		self.reddit = praw.Reddit(client_id='kCrm1Fz7g6alMw',
	        	client_secret='z3l8kIhB9zYAQl7QUobTOkBGCnQ',
	                user_agent='testscriptplswork',
	                username='joshdunigan',
	                password='joshdunigan123')
		self.subreddit = self.reddit.subreddit(nameOfSubreddit)
		self.returnList = []
		self.iteratethis = self.subreddit.top(time_filter = 'day', limit = limits)

	def getSubredditName(self):
		return self.nameOfSubreddit

	def setSubreddit(self, subredditName):
		self.nameOfSubreddit = subredditName
	
	#following functions only print from hot and of the top 10. Can change it by changing the "hot" and the limit to a higher or lower number. All require a String parameter that state the subreddit you want.

	#get the image link for the top 10 in hot section. Returns list filled with url. Param limit 

	def getImageUrl(self):
		for submission in self.iteratethis:
	   		self.returnList.append(submission.url)
		return self.returnList

	#gets the title for the top 10 in hot section. Returns list of Titles.
	def getTitle(self):
		for submission in self.iteratethis:
	   		self.returnList.append(submission.title)
		return self.returnList

	#gets the score. Returns list of scores.
	def getScore(self):
		for submission in self.iteratethis:
	   		self.returnList.append(submission.score)
		return self.returnList

