from quote import get_quote
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables file

# Set the access keys for Twitter
auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_SECRET_KEY"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

# Set up the Twitter API
api = tweepy.API(auth)

# Tweets the quote
api.update_status(get_quote())
