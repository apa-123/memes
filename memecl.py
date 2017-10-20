
class Memes:
	"""A meme object. A meme object has the following properties:

	Attributes:
	title: A string representing the meme's title
	url: A string representing the meme's url
	subreddit: The subreddit of the meme
	score: A float number representing the score the meme gets
	"""

	def __init__(self, title, url, subreddit, score):
		"""Return a Meme object whose title is *title*, url is *url*,
		subreddit is *subreddit*, score is *score*.
		"""
		self.title = title
		self.url = url
		self.subreddit = subreddit
		self.score = score
		
	def get_title(self):
		"""Return a string representing the title of the meme."""
		return self.title
	
	def get_URL(self):
		"""Return a string representing the url of the meme."""
		return self.url
	
	def get_subreddit(self):
		"""Return the subreddit of the meme."""
		return self.subreddit

	def get_score(self):
		"""Return a float number representing the score of the meme."""
		return self.score

	def set_title(self, title):
		"""Set the string representing the title of the meme to *title*."""
		self.title = title

	def set_URL(self, url):
		"""Set the string representing the url of the meme tp *url*."""
		self.url = url

	def set_subreddit(self, subreddit):
		"""Set the subreddit of subreddit to *subreddit*."""
		self.subreddit = subreddit
		
	def set_score(self, score):
		"""Set the float number representing the score of 
		subreddit to *score*."""
		self.score = score	

	def display(self):
		"""Prints out all the information about the meme."""
		print("title = " + self.title, "URL = " + self.url, \
			"Subreddit = " + self.subreddit, "Score = " + str(self.score))

	def __str__(self):
		"""Return the string representation of the information in the 
		meme object. Defined function in python that enables users to call 
		with reference to any meme."""		
		return "title = " + self.title + "URL = " + self.url \
		+ "Subreddit = " + self.subreddit + "Score = " + str(self.score)

	def __lt__(self, other):
		"""Compares the scores of two memes and returns if one is 
		lower than another"""
		if self.score < other.score:
			return True
		else:
			return False




