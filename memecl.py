
class Memes:

	def __init__(self, title, url, subreddit, score):
		self.title = title
		self.url = url
		self.subreddit = subreddit
		self.score = score


	def getTitle(self):
		return self.title

	def getURL(self):
		return self.url

	def getSubreddit(self):
		return self.subreddit

	def getScore(self):
		return self.score

	def setTitle(self, title):
		self.title = title

	def setURL(self, url):
		self.url = url

	def setSubreddit(self, subreddit):
		self.subreddit = subreddit

	def setScore(self, score):
		self.score = score	

	def display(self):
		print("title = " + self.title, "URL = " + self.url, "Subreddit = " + self.subreddit, "Score = " + str(self.score))

	def __str__(self):
		return "title = " + self.title + "URL = " + self.url + "Subreddit = " + self.subreddit + "Score = " + str(self.score)

	def __lt__(self, other):
        if self.score < other.score:
            return True
        else:
            return False




