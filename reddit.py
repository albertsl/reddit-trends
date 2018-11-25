import praw

class Reddit:
	def __init__(self, credentials):
		client_id, client_secret, user_agent, username, password = credentials
		self.reddit = praw.Reddit(client_id=client_id, 
						client_secret=client_secret,
						user_agent=user_agent,
						username=username,
						password=password)

	def get_popular_subs(self, limit=100):
		popular_subs = self.reddit.subreddits.popular(limit=limit)
		
		l=[]
		for item in popular_subs:
			l.append(item)
		
		return l
