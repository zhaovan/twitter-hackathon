import tweepy
import credentials
import pandas as pd


auth = tweepy.OAuthHandler(credentials.consumer_key,
                           credentials.consumer_secret)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)

# This can be used for #s and ip of the user
def getTweets (keyWord):
    keyWord = keyWord + " -filter:retweets" # Filters retweets
    tweets = tweepy.Cursor(api.search,
                       q=keyWord).items(5) # only returns 5 tweets, but it can be changed
    tweetsList = []
    for tweet in tweets:
        tweetElement = [tweet.user.screen_name,tweet.text, tweet.id]
        try:
            tweetElement.append(tweet.place.id) # If the user doesnt share their location
        except:
            tweetElement.append(None)
        try:
            tweetElement.append(tweet.possibly_sensitive) # This field only surfaces when a Tweet contains a link
        except:
            tweetElement.append(None)
        tweetsList.append(tweetElement)
    # DataFrame with the users (string), the tweet (string), the tweet id (Int64)
    # their location where the tweet was made (coordinates) and if the tweet is sensitive (boolean)
    tweet_text = pd.DataFrame(data=tweetsList,
                              columns=['user',  "tweet", "tweetID", "location", "sensitive"])
    return tweetsList

# function to get the text of each tweet for the other api we are using
def getTweetsText(tweetsList):
    tweetsList.get("tweet")
    





# print(getTweets("74.125.19.104"))
# print(getTweets("#cats"))
