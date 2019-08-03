import json
import requests
from requests_oauthlib import OAuth1

api_key = '' # enter api key
api_secret_key = '' # enter api secret key
auth = OAuth1(api_key, api_secret_key)

screen_name="thevirdas"
url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+screen_name+"+&count=200"

ans=requests.get(url,auth=auth)
j_ans=json.loads(ans.text)
j_ans

for text in j_ans:
    print(text["text"])
    print("\n")
   
