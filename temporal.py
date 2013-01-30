#!/usr/bin/python
'''
get a current bag of words from twitter based on a key word for a value of "current sentiment".
'''

import emotiscrape
import get_tweets

emo = emotiscrape.Emotiscrape()
tw = get_tweets.GetTweets()

bag = tw.get_tweets("$NFLX")
o = emo.analyze_string(bag)

print "[Temporal] %s, %s probability" % (o.get("classification"), o.get("probability_delta"))