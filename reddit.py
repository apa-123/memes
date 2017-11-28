import praw 
# Python Reddit API Wrapper. https://praw.readthedocs.io/en/latest/. Praw allows us to access Reddit API and helps us parse the data from the Reddit API.
class Reddit:

	def __init__(self, nameOfSubreddit, limits):
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
		#Initializies a list used to return the information.
		self.returnList = []
		#Gets the limits number of posts from the "top" section of the subreddit.
		self.posts = self.subreddit.top(time_filter = 'day', limit = limits)
	#Return the name of the Subreddit.
	def getSubredditName(self):
		return self.nameOfSubreddit
	#Changes the subreddit name.
	#@param Name of the subreddit you want to change to.
	def setSubreddit(self, subredditName):
		self.nameOfSubreddit = subredditName
		self.subreddit = self.praw.subreddit(nameOfSubreddit)
	#Returns a list full of Urls of the 
	def getImageUrl(self):
		self.returnList = [submission.url for submission in self.posts]
		return self.returnList
	#Returns a list of titles of the posts given the 
	def getTitle(self):
		self.returnList = [submission.title for submission in self.posts]
		return self.returnList
	#Returns a list of ints of scores of the posts.
	def getScore(self):
		self.returnList = [submission.score for submission in self.posts]
		return self.returnList
	#Returns a list of the usernames who submitted the posts.
	def getAuthor(self):
		self.returnList = [submission.author for submission in self.posts]
		return self.returnList
