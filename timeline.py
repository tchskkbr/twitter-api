# CONSUMER_KEY        = 'YOUR_CONSUMER_KEY'
# 2	CONSUMER_SECRET_KEY = 'YOUR_CONSUMER_SECRET_KEY'
# 3	ACCESS_TOKEN        = 'YOUR_ACCESS_TOKEN'
# 4	ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'
CONSUMER_KEY = "cJ5TmcbtGVpenfVDgFGI9vQn0"
CONSUMER_SECRET_KEY = "8T06UvNpFuRE6VjcGmcoL5w5sl7oKoDpIH6ihTCdznVj77wVxX"
ACCESS_TOKEN = "1652521808-fHKwELBeOTjJId3xO8toheiXcTCqO6JuVT8SoGZ"
ACCESS_TOKEN_SECRET = "fkSOz7WhzHKFzGHY84eic2zHiPmby9T6aZutFl8jjAPqr"
# 5	import config
from twitter import *

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))
	
timelines = t.statuses.home_timeline()
for timeline in timelines:
    tl = '({id}) [{username}]:{text}'.format(
        id=timeline['id'], username=timeline['user']['name'], text=timeline['text'])
    print (tl)