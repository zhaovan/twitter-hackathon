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


def getTweets(keyWord, nums=10):
    keyWord = keyWord + " -filter:retweets"  # Filters retweets
    tweets = tweepy.Cursor(api.search,
                           q=keyWord, result_type="popular", tweet_mode="extended").items(int(nums))  # only returns 5 tweets, but it can be changed
    # DataFrame with the users (string), the tweet (string), the tweet id (Int64)
    # their location where the tweet was made (coordinates) and if the tweet is sensitive (boolean)
    tweetsList = pd.DataFrame()
    for tweet in tweets:
        print(tweet.full_text)
        tweetElement = [tweet.user.screen_name,
                        tweet.full_text, tweet.id]
        try:
            # If the user doesnt share their location
            tweetElement.append(tweet.place.id)
        except:
            tweetElement.append(None)
        try:
            # This field only surfaces when a Tweet contains a link
            tweetElement.append(tweet.possibly_sensitive)
        except:
            tweetElement.append(None)
        tweet_serie = pd.Series({"user": tweetElement[0],
                                 "tweet": tweetElement[1],
                                 "tweetID": tweetElement[2],
                                 "location": tweetElement[3],
                                 "sensitive": tweetElement[4]})
        tweetsList = tweetsList.append(tweet_serie, ignore_index=True)
    return tweetsList

# function to get the text of each tweet for the other api we are using
# returns list with the texts of wach tweet


def get_tweets_user(tweetsList):
    users = tweetsList["user"]
    user_list = []

    for user in users:
        user_list.append(user)

    return user_list


def getTweetsText(tweetsList):
    texts = tweetsList["tweet"]

    textList = []
    links = []
    for text in texts:
        data = text.split("https://")  # Separates the urls
        textList.append(data[0])
    return textList

# funtion that changes the data frame to a json


def getJson(tweetList):
    json = tweetList.to_json()
    return json
