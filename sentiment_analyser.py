import tweepy
from textblob import TextBlob
import numpy as np 
import operator
import csv

consumer_key = '7rK9Xi9s4EDv7vPGhSHCzj0ah'
consumer_secret = '0PDnuQPbMTy8vJeyAj011jcjyIlm4VWEsw1Qu6uX2vwr6SOWPo'

access_token = '468850724-gxWQjmomX4X6qw7CoEZqR3NaHd0Yyg1ikQi2I1oz'
access_token_secret = '2s6Q87MulwzHfw36yAdPNaNRCOMKKsi88SPGMwnQBQ0D8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Kobe Bryant')
                
for tweety in public_tweets:
	print(tweety.text)
	analysis = TextBlob(tweety.text)
	print(analysis.sentiment)


with open('tweets.csv', 'wb') as datas:
	datas.write('tweet,sentiment_label\n')
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		wr = csv.writer(datas, dialect='excel')
		wr.writerow(tweet.text.encode('utf8'))
		#datas.write('%s,%s' % (tweet.text.encode('utf8'), get_label(analysis)))
		#csvwriter.writerow(line)
		#csvwriter.writerow('/n')