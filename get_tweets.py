import tweepy
import credentials


auth = tweepy.OAuthHandler(credentials.consumer_key,
                           credentials.consumer_secret)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

def getTweets (keyWord, date):
    tweets = tweepy.Cursor(api.search,
                       q=keyWord,
                       lang="en",
                       since=date).items(5)
    for tweet in tweets:
        print(tweet.text)


getTweets("#cats","2017-04-03")

