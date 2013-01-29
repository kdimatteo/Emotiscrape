#!/usr/bin/python

import emotiscrape

emo = emotiscrape.Emotiscrape()
print emo.analyze_string("this is a truely awesome utility. I can't wait to hook it up to Taggy!")
print emo.analyze_string("$AAPL")