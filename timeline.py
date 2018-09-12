"""
before do this file, you should register twitter developer account.
It is necessary to have your four KEY.
"""

# CONSUMER_KEY        = 'YOUR_CONSUMER_KEY'
# 2	CONSUMER_SECRET_KEY = 'YOUR_CONSUMER_SECRET_KEY'
# 3	ACCESS_TOKEN        = 'YOUR_ACCESS_TOKEN'
# 4	ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

import config # import config.py
from twitter import *

t = Twitter(auth=OAuth(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET_KEY))
	
timelines = t.statuses.home_timeline()
for timeline in timelines:
    tl = '({id}) [{username}]:{text}'.format(
        id=timeline['id'], username=timeline['user']['name'], text=timeline['text'])
    print (tl) # output timeline