#!/usr/bin/python

'''
Script to pull tweets to create sentiment dimensions.

'''

import fileinput
import json
import re
import urllib
import urllib2
import time

class GetTweets():
    
    def __init__(self):
        self.lastID = 0

    def get_and_write_tweets(self, term, filename):
        content = self.get_tweets(term, since_id=self.lastID)
        if(content):
            file = open(filename, 'a')
            file.write(content)
            file.close()
        
        
    def get_tweets(self, hash_tag, page=1, rpp=100, since_id=0):
        u = 'http://search.twitter.com/search.json?lang=en&since_id=%s&rpp=%s&page=%s&result_type=recent&q=%s' % (str(since_id), str(rpp), str(page), urllib.quote_plus(hash_tag))
        ID_list = []
        
        try:
            result = urllib2.urlopen(u)
            o = json.loads(result.read())
            content = ""
            L = []
            for tweet in o['results']:
                myTweet = self.cleanup_tweet(tweet['text'], hash_tag)
                L.append(myTweet) 
                ID_list.append(tweet['id'])
            
            if(len(L) == 100):
                #get the last ID,
                ID_list = sorted(ID_list, reverse=True)
                self.lastID = ID_list[0]
                
                print "[GetTweets] %s logged %s messages. End id: %s" % (hash_tag, len(L), self.lastID)
                #ok done with this function
                return "".join(L).encode("utf-8")
            else:
                print "[GetTweets] not enuff messages for %s. Length only %s" % (hash_tag, len(L))
                return False
            
        except:
            print "[GetTweets] Todo: Failure message here. %s " % u
            return False
        
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
    ## run
    while 1:
        o = GetTweets()
        o.get_and_write_tweets(':)', 'output/good.txt')
        p = GetTweets()
        p.get_and_write_tweets(':(', 'output/bad.txt')
        time.sleep(5)
