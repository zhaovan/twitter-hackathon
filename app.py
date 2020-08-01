from flask import Flask
import get_tweets

app = Flask(__name__)


@app.route('/')
def home_page():
    get_tweets()
    return "home_page"
