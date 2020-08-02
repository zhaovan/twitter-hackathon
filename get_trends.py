import tweepy
import credentials

auth = tweepy.OAuthHandler(credentials.consumer_key,
                           credentials.consumer_secret)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)


def get_trends(lat, longi):
    json_val = api.trends_closest(float(lat), float(longi))
    print(json_val[0])
    trending = api.trends_place(json_val[0]["woeid"])
    return trending
