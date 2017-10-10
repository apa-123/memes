import praw

reddit = praw.Reddit(client_id='kCrm1Fz7g6alMw',
                     client_secret='z3l8kIhB9zYAQl7QUobTOkBGCnQ',
                     user_agent='testscriptplswork',
                     username='joshdunigan',
                     password='joshdunigan123')
subreddit = reddit.subreddit('dankmemes')
print(subreddit.display_name)
for submission in subreddit.hot(limit=10):
    print(submission.title)   
    print(submission.url)

