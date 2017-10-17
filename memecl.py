
class Memes:
#Defines the class, this function is needed in all python code
	def __init__(self, title, url, subreddit, score):
		self.title = title
		self.url = url
		self.subreddit = subreddit
		self.score = score
		
#takes self as an input and returns the title, enabling users to call this function to get the title
	def getTitle(self):
		return self.title
	
#takes self as an input and returns the URL, enabling users to call this function to get the URL
	def getURL(self):
		return self.url
	
#takes self as an input and returns the subreddit, enabling users to call this function to get the subreddit
	def getSubreddit(self):
		return self.subreddit

#takes self as an input and returns the score, enabling users to call this function to get the score
	def getScore(self):
		return self.score

#takes self and title as an input and sets the title
	def setTitle(self, title):
		self.title = title

#takes self and URL as an input and sets the URL
	def setURL(self, url):
		self.url = url

#takes self and subreddit as an input and sets the subreddit
	def setSubreddit(self, subreddit):
		self.subreddit = subreddit
		
#takes self and score as an input and sets the score
	def setScore(self, score):
		self.score = score	

#prints out all of the information about the meme
	def display(self):
		print("title = " + self.title, "URL = " + self.url, "Subreddit = " + self.subreddit, "Score = " + str(self.score))

#defined function in python that enables users to call with reference to any meme
	def __str__(self):
		return "title = " + self.title + "URL = " + self.url + "Subreddit = " + self.subreddit + "Score = " + str(self.score)

#compares the scores of two memes and returns if one is lower than another
	def __lt__(self, other):
        if self.score < other.score:
            return True
        else:
            return False




