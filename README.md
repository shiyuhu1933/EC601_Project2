# EC601_Project2
Twitter API data pulling and analyze sentiment by Google Cloud NLP

## Product Mission
Implement twitter API to retrieving tweets from twitter and analyze sentiment of tweets by using the
Google Natual Language API.The Twitter API is able to allow tools like Adverity to regularly retrieve tweets information. 
Users can then implement sentiment analysis from Google Natural Language Process 

## User Story and MVP
As an analyst from PR agency, it is important to know the customer feedback of their new released products as well as
the reputation of their chosen brand ambassadors. Also, as an investor, it is important to analyze related information
about the stock markets.
A program that takes any tweets as input and ouput a sentiment scale of sentiment. Tweets will be the input from the Twitter api. The result from twitter api will be analyzed by google Natural Language Processing. In this way, the user is able to know the sentiment of tweets.

## Environment Setup
Python 3.0+

Tweepy

Google Colab

Google Cloud Natual Language V1

## Steps and Resutls

First, to get the permissions to call from Twitter, regist a Twitter account as well as getting
API_Key, API_Key_Secret, Access_token, Access_token_secret.

```Python
consumer_key ='Your API key/consumer key'
consumer_secret = 'Your secret API key/ consumer key'
access_token = 'Your access token'
access_token_secret = 'Your secret access token'
Bearer_token ='Your bearer token' 
```

For example, tweets from Elon Reeve Musk will be retrieved by passing the
username of the account you want to download.

![image](https://github.com/shiyuhu1933/EC601_Project2/blob/main/Tweets.png)


To begin with, regist a account for Google Cloud, and create a project and enable it for Google NLP access as well as creating credentials for a service account: https://cloud.google.com/natural-language

Next, get the configuration of keys for the project with the following steps:
In the Cloud Console, click the email address for the service account that you created.
1.Click and Add Keys.
3.Get a JSON key file and uplpoad it to the google dirve if using Google Colab.

```Python
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "JSon file Path"
```

The Sentiment of Musk's tweets then could be analyzed:
```Python
mentions {
    text {
      content: "SpaceX"
      begin_offset: 80
    }
    type: PROPER
    sentiment {
      magnitude: 0.10000000149011612
      score: -0.10000000149011612
    }
  }
  sentiment {
    magnitude: 0.10000000149011612
    score: -0.10000000149011612
  }
}
```

REFERCENCE:
https://cloud.google.com/natural-language/docs/samples 













