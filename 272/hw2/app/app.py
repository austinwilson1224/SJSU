from flask import Flask, render_template, request
import tweepy
from keys import consumer_key, consumer_secret, access_token, access_token_secret

# print(consumer_key, consumer_secret, access_token, access_token_secret)

# authorization 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

me = api.me()
name = me.screen_name
tweets = api.user_timeline(name)

tweets = [
    "test tweet 1",
    "test 2",
    "some random useless stuff",
    "the latest and greatest"
]







app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        content = request.form['content']
        tweets.push(content)
        # new_status = api.update_status(content)
        print(content)

    return render_template("index.html", name=name, tweets=tweets)

@app.route("/status", methods=["GET", "POST"])
def post_status():

    return render_template("post_status.html", name=name)

@app.route("/test_get", methods=["GET"])
def get_latest():
    for tweet in tweets:

        print(tweets[0].text)
        print("\n\n")
    return 'test'

@app.route("/status2", methods=["GET"])
def get_status():
    pass


@app.route("/remove_status", methods=["GET", "DELETE"])
def remove_status():
    return render_template("remove_status.html", tweets=tweets)





if __name__ == "__main__":
    app.run(debug=True)