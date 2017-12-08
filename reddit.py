# Python Reddit API Wrapper. https://praw.readthedocs.io/en/latest/. Praw allows us to access Reddit API and helps us parse the data from the Reddit API.
import praw 


class Reddit:

	def __init__(self, nameOfSubreddit, limits):
		"""Init Reddit Class"""

		
		#Initializies the name of the subreddit.
		self.nameOfSubreddit = nameOfSubreddit


		#Initializies the amount of posts you retrieve from reddit.
		self.limits = limits


		#Initializies an instance of Reddit. Need account and application information to access it.
		self.praw = praw.Reddit(client_id='kCrm1Fz7g6alMw',
	        	client_secret='z3l8kIhB9zYAQl7QUobTOkBGCnQ',
	                user_agent='testscriptplswork',
	                username='joshdunigan',
	                password='joshdunigan123')


	    #Initializes the subreddit. 
		self.subreddit = self.praw.subreddit(nameOfSubreddit)


		#Initializies a list used to return the information


		self.urlList = []
		self.titleList = []
		self.authorList = []
		self.scoreList = []

	def getSubredditName(self):
		"""	Return the name of the Subreddit."""
		return self.nameOfSubreddit

	def setSubreddit(self, subredditName):
		"""Changes the subreddit name. @param Name of the subreddit you want to change to."""
		self.nameOfSubreddit = subredditName
		self.subreddit = self.praw.subreddit(nameOfSubreddit)

	def getImageUrl(self):
		for submissions in self.subreddit.top(time_filter = 'day', limit = self.limits):
			self.urlList.append(submissions.url)
		return self.urlList

	def getTitle(self):
		for submissions in self.subreddit.top(time_filter = 'day', limit = self.limits):
			self.titleList.append(submissions.title)
		return self.titleList

	def getScore(self):
		"""Returns a lists of integers of scores of the posts."""
		self.scoreList = [submissionsss.score for submissionsss in self.subreddit.top(time_filter = 'day', limit = self.limits)]
		return self.scoreList

	def getAuthor(self):
		"""Returns a list of the usernames who submtited the posts."""
		self.authorList = [submission.author for submission in self.subreddit.top(time_filter = 'day', limit = self.limits)]
		return self.authorList
