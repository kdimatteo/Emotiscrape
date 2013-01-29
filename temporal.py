#!/usr/bin/python
'''
get a current bag of words from twitter based on a key word, use a temporal dimension for sentiment.
'''

import emotiscrape
import get_tweets

emo = emotiscrape.Emotiscrape()
tw = get_tweets.GetTweets()

bag = tw.get_tweets("$NFLX")
L = emo.analyze_string(bag)

print "%s, %s probability" % (L[1], L[0])