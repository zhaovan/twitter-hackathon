import tweepy
import credentials
import pandas as pd


auth = tweepy.OAuthHandler(credentials.consumer_key,
                           credentials.consumer_secret)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)

# This can be used for #s and ip of the user
# returns dataframe with the info of the tweets
def getTweets (keyWord):
    keyWord = keyWord + " -filter:retweets" # Filters retweets
    tweets = tweepy.Cursor(api.search,
                       q=keyWord).items(5) # only returns 5 tweets, but it can be changed
    # DataFrame with the users (string), the tweet (string), the tweet id (Int64)
    # their location where the tweet was made (coordinates) and if the tweet is sensitive (boolean)
    tweetsList = pd.DataFrame()
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
        tweet_serie = pd.Series({"user" : tweetElement[0],
                                 "tweet" : tweetElement[1],
                                 "tweetID" : tweetElement[2],
                                 "location" : tweetElement[3],
                                 "sensitive" : tweetElement[4]})
        tweetsList = tweetsList.append(tweet_serie,ignore_index=True)
    return tweetsList

# function to get the text of each tweet for the other api we are using
# returns list with the texts of wach tweet
def getTweetsText(tweetsList):
    texts = tweetsList["tweet"]
    textList = []
    for text in texts:
        data = text.split("https://") # Separates the urls
        textList.append(data[0])
    return textList

# function that changes the data frame to a json
def getJson(tweetList):
    json = tweetList.to_json()
    return json

# print(getTweets("74.125.19.104"))
# print(getTweets("#cats"))
# print(getTweetsText(getTweets("#cats")))
# print(getJson(getTweets("#cats")))