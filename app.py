from flask import Flask
from get_tweets import *

app = Flask(__name__)


@app.route('/<name>')
def home_page(name):
    listOfData = getTweets("#live","2017-04-03")
    return listOfData

if __name__ == "__main__":
    app.run(debug=True)
