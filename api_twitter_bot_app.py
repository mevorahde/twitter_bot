import tweepy
import time
import os
from dotenv import load_dotenv
from pathlib import Path

# Activate '.env' file
load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

auth = tweepy.OAuthHandler(os.getenv("t_key"), os.getenv("t_key_password"))
auth.set_access_token(os.getenv("t_access_token"), os.getenv("t_access_token_secret"))

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search_terms = ["#100DaysOfCode", "#CodeNewbie", "#Python", "#CSharp"]
number_of_tweets = 25
search = None
for item in search_terms:
    search = item
    for tweet in tweepy.Cursor(api.search, q=search).items(number_of_tweets):
        try:
            print("Tweet Liked")
            tweet.favorite()
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
