from flask import Flask, jsonify
import get_tweets
import time

from get_tweets import getTweets, getTweetsText, getJson, get_tweets_user
from sentiment_analysis import get_text_sentiment

from get_trends import get_trends

app = Flask(__name__)


# @app.route('/')
# def home_page():
#     # get_tweets()
#     return "home_page"


@app.route('/<query>/<nums>')
def get_tweets_by_query(query, nums):
    tweets_list = getTweets(query, nums)

    tweet_texts = getTweetsText(tweets_list)
    users = get_tweets_user(tweets_list)

    sentiment = []
    for tweet in tweet_texts:
        sentiment.append(get_text_sentiment(tweet))
    return jsonify(tweets=tweet_texts, sentiments=sentiment, users=users)


@app.route('/trends/<lat>/<longit>')
def get_trends_for_page(lat, longit):
    return jsonify(trends=get_trends(lat, longit))
