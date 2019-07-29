import requests
import json
from requests_oauthlib import OAuth1

api_key="Z0P4OidK4cKttEmzDdQRSckpa"
api_secret="rqpAf5m3pbnoanYR1Z5BLYFkksiuxhwOQzhv8PeVmHsa7rXySR"

auth=OAuth1(api_key,api_secret)

keyword='dogs'

url = "https://api.twitter.com/1.1/search/tweets.json?q="+keyword+"&count=200&tweet_mode=extended&lang=en&result_type=popular"

ans=requests.get(url,auth=auth)
jtweet=json.loads(ans.text)


for tweet in jtweet['statuses']:
    print(tweet['full_text'])
    print('\n')
