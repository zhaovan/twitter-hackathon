import tweepy
import credentials
import pandas as pd


auth = tweepy.OAuthHandler(credentials.consumer_key,
                           credentials.consumer_secret)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

def getTweets (keyWord, date):
    keyWord = keyWord + " -filter:retweets" # Filters retweets
    tweets = tweepy.Cursor(api.search,
                       q=keyWord,
                       lang="en",
                       since=date).items(5)
    tweetsList = []
    for tweet in tweets:
        tweetElement = [tweet.user.screen_name,tweet.text]
        try:
            tweetElement.append(tweet.coordinates.coordinates)
        except:
            tweetElement.append(None)
        try:
            tweetElement.append(tweet.possibly_sensitive)
        except:
            tweetElement.append(None)
        tweetsList.append(tweetElement)
    # DataFrame with the users (string), the tweet (string),
    # their location where the tweet was made (coordinates) and if the tweet is sensitive
    tweet_text = pd.DataFrame(data=tweetsList,
                              columns=['user', "location", "tweet", "sensitive"])
    print(tweetsList)



#getTweets("#cats","2017-04-03")

