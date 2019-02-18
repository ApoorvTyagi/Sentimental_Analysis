#importing required dependencies
import tweepy
from textblob import TextBlob 

# keys and tokens from the Twitter Development Console for authenticating twitter
key="XXXXXXXXXXXXXXXXXXXX"
secret_key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
secret_token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

authentication=tweepy.OAuthHandler(key,secret_key)
authentication.set_access_token(access_token,secret_token)

api=tweepy.API(authentication)

#search tweets having certain key word
tweets=api.search("any-content-here")#type the key word you want to analyze tweets about

for tweet in tweets:
    print(tweet.text)#printing every tweet
    analyze=TextBlob(tweet.text)#analysing sentiments of each tweet
    print(analyze.sentiment)
    # setting sentiment 
    if analyze.sentiment.polarity > 0: 
        print('positive')
    elif analyze.sentiment.polarity == 0: 
        print('neutral')
    else: 
        print('negative')
    print()
