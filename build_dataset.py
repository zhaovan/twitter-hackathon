import pandas as pd
from get_tweets import getTweet


def getDataGossipcopFake():
    cvc = pd.read_csv("dataset/gossipcop_fake.csv")
    for id in cvc["tweet_ids"]:
        text = getTweet(id)
        cvc["text"] = text
        cvc["status"] = 1


getDataGossipcopFake()


def getDataGossipcopReal():
    cvc = pd.read_csv("dataset/gossipcop_real.csv")
    for id in cvc["tweet_ids"]:
        text = getTweet(id)
        cvc["text"] = text
        cvc["status"] = 0


getDataGossipcopReal()


def getDataPolitifactFake():
    cvc = pd.read_csv("dataset/politifact_fake.csv")
    for id in cvc["tweet_ids"]:
        text = getTweet(id)
        cvc["text"] = text
        cvc["status"] = 1


getDataPolitifactFake()


def getDataPolitifactReal():
    cvc = pd.read_csv("dataset/politifact_real.csv")
    for id in cvc["tweet_ids"]:
        text = getTweet(id)
        cvc["text"] = text
        cvc["status"] = 0


getDataPolitifactFake()


def createDataBase():
    df = pd.DataFrame()
    df.append(pd.read_csv("dataset/politifact_fake.csv"))
    df.append(pd.read_csv("dataset/politifact_real.csv"))
    df.append(pd.read_csv("dataset/gossipcop_fake.csv"))
    df.append(pd.read_csv("dataset/gossipcop_real.csv"))
    df.reset_index(inplace=True, drop=True)
    df.to_csv('dataset.csv', index=False)


createDataBase()
