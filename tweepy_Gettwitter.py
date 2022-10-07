# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tweepy #https://github.com/tweepy/tweepy
import json
#consumer_key ='Your API key/consumer key'
#consumer_secret = 'Your secret API key/ consumer key'
#access_token = 'Your access token'
#access_token_secret = 'Your secret access token'
#Bearer_token ='Your bearer token'
consumer_key = 'jSIaIOgiLNYjTZXtpnZhiO2wk'
consumer_secret = '01LBXE6ojXv3vikLpu6w8KMiMYVn6zT25mZFu0WXoijONWuvJC'
access_token = "1576044567178186752-Dc3aW6fuQfr6mhi3tE2Yk5VQAVQKdG"
access_token_secret = "wIVicLJz3cKtLoLocIqyYenoxKLPLWqhjBvJZbThkWRZx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


import json
import csv
import tweepy
import re
import yweather
import pandas as pd

import os
from google.cloud import language_v1

access_key = "1576044567178186752-Dc3aW6fuQfr6mhi3tE2Yk5VQAVQKdG"
access_secret = "wIVicLJz3cKtLoLocIqyYenoxKLPLWqhjBvJZbThkWRZx"


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=10)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if (len(alltweets) > 15):
            break
        print(f"...{len(alltweets)} tweets downloaded so far")

        # write tweet objects to JSON
    file = open('tweet.json', 'w')
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json, file, sort_keys=True, indent=4)

    # close the file
    print("Done")
    file.close()


def printTweet(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(screen_name=screen_name, count=10)
    for tweet in public_tweets:
        print(tweet.text)
    # Get the User object for twitter...
    user = api.get_user(screen_name=screen_name)
    print("=" * 20)
    print(f'User name: @{user.screen_name}')
    print(f'Total followers: {user.followers_count}')
    print('List of following accounts:')
    for friend in user.friends():
        print(friend.screen_name)


def searchTweets(q, count=100):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    searchResult = api.search(q=q, count=count)
    for result in searchResult:
        print(result.text)
        # print(searchResult)


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("@elonmusk")
    printTweet("@elonmusk")
    searchTweets('SpaceX')
