import praw #reddit wrapper, helps parse json. Short for python reddit api wrapper. Must install it to run it.  

#following is trying to get reddit json. To get a short description of the subreddit, go to reddit.com/reddits. Then get the json of /reddits and parse it to find the "public description" and get the string afterward to get the short description. Haven't found any other way of finding short description. Haven't done so yet.
'''
import json
#import requests

#r = requests.get(
    'https://reddit.com/reddits.json',
    headers={'User-Agent': ''}
)
r.text # Unformatted text

reddit_json = json.loads(r.text)
reddit_json
'''

#returns reddit instance. Can probably make a class of reddit but haven't done so yet.
def getReddit():
	reddit = praw.Reddit(client_id='kCrm1Fz7g6alMw',
        	client_secret='z3l8kIhB9zYAQl7QUobTOkBGCnQ',
                user_agent='testscriptplswork',
                username='joshdunigan',
                password='joshdunigan123')	
	return reddit
#following functions only print from hot and of the top 10. Can change it by changing the "hot" and the limit to a higher or lower number. All require parameter that state the subreddit you want.

#get the image link for the top 10 in hot section. Returns list filled with url.
def getImageUrl(getSubreddit):
	reddit = getReddit()
	subreddit = reddit.subreddit(getSubreddit)
	returnList = []
	for submission in subreddit.hot(limit=10):
   		returnList.append(submission.url)
	return returnList

#gets the title for the top 10 in hot section. Returns list of Titles.
def getTitle(getSubreddit)
	reddit = getReddit()
	subreddit = reddit.subreddit(getSubreddit)
	returnList = []
	for submission in subreddit.hot(limit=10):
   		returnList.append(submission.title)
	return returnList

#gets the score. Returns list of scores.
def getTitle(getSubreddit)
	reddit = getReddit()
	subreddit = reddit.subreddit(getSubreddit)
	returnList = []
	for submission in subreddit.hot(limit=10):
   		returnList.append(submission.score)
	return returnList


#testing section
'''

reddit = praw.Reddit(client_id='kCrm1Fz7g6alMw',
        client_secret='z3l8kIhB9zYAQl7QUobTOkBGCnQ',
        user_agent='testscriptplswork',
        username='joshdunigan',
        password='joshdunigan123')	
wikipage = reddit.subreddit('iama').wiki['proof']
print(wikipage.content_md)
#wikipage = reddit.subreddit('dogs').wiki['description']
#print(wikipage.content_md)
#for page in reddit.subreddit('dogs').wiki:
	#print(page)
'''
