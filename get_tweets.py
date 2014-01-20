#!/user/bin/python

import os
import fileinput
import re
from twitter import *
from TwitterSearch import *

class GetTweets():

    def __init__(self, term, outfile):
        

        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CONSUMER_SECRET']



        file = open(outfile, 'a')

        try:
            tso = TwitterSearchOrder() 
            tso.setKeywords([term])
            tso.setLanguage('en')
            tso.setCount(99) 
            tso.setIncludeEntities(False) # don't give us all those entity information

            MY_TWITTER_CREDS = os.path.expanduser('.app_credentials')

            if not os.path.exists(MY_TWITTER_CREDS):
                oauth_dance("emotiscrape", CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

            oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)


            t = TwitterSearch(
                consumer_key = CONSUMER_KEY,
                consumer_secret = CONSUMER_SECRET,
                access_token = oauth_token,
                access_token_secret = oauth_secret
            )


            for tweet in t.searchTweetsIterable(tso): # this is where the fun actually starts :)
                cleanTweet = self.cleanup_tweet(tweet['text'], term).encode('utf-8')
                file.write(cleanTweet)
                #print cleanTweet
                #print tweet['created_at'] , '\t',  tweet['text']
                #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
                print "pulled 99 tweets for %s, until %s [%s]" % (term, tweet['created_at'], tweet['id'])

        except TwitterSearchException as e: 
            # take care of all those ugly errors if there are some
            print(e)




    def cleanup_tweet(self, s, term):
       
        # drop links
        pattern = '((mailto\:|(news|(ht|f)tp(s?))\://){1}\S+)'
        s = re.sub(pattern, '', s) 
        
        # drop @replies
        s = re.sub('(@){1}\S+', '', s) 
        
        # drop hastags
        s = re.sub('(#){1}\S+', '', s) 
        
        # drop the search term
        s = s.replace(term, '') 
        
        #remove double spaces
        s.replace('  ', '')
        
        return s.strip()



if __name__ == "__main__":
    # run forever
    while 1:
        o = GetTweets(':)', "output/good.txt")
        #p = GetTweets(':(', "output/bad.txt")

