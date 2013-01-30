Emotiscrape
===========

Includes a few things:

+ get_tweets.py - Mine Twitter to create corpa, Thanks to ["Sentiment Analysis and Opinion Mining" Alexander Pak, Patrick Paroubek][http://www.cs.cornell.edu/home/llee/omsa/omsa.pdf]

+ emotiscrape.py - Create a NLTK training set from the generated corpa.

+ test.py - A sample implementation


Implementation
--------------
```
import emotiscrape

emo = emotiscrape.Emotiscrape()
o = emo.analyze_string("$AAPL")
print o.keys()

#yields:
["probability_pos", "probability_neg", "probability_delta", "classification", "original_text"}

```


Running the script alone will test a list of phrases against the training set:

```
$ python emotiscrape.py
cleaned 40000 tweets from good.txt
cleaned 40000 tweets from bad.txt
---------
TEST MODE
---------
[pass] pos : 62.6147357976 		 i love you harry!
[pass] neg : 41.224592175 		 This is incredibly annoying, i hate working here and i hate this crummy application
[fail] pos : 75.7709251101 		 You are a terrible person and everything you do is bad.
[pass] pos : 97.8968818172 		 I love you all and you make me happy
[pass] neg : 12.1708961999 		 I frown whenever I see you in a poor state of mind
[pass] pos : 92.2536382568 		 Finally getting rich from my ideas. They make me smile
[pass] neg : 82.9726651481 		 My mommy is poor
[pass] pos : 56.324917113 		 I love butterflies. Yay for happy
[pass] neg : 49.93756813 		 Everything is fail today and I hate stuff
[pass] pos : 15.3846153846 		 Larry is my friend, but boy is he shady
```


Todo
----

+ move prints to log()