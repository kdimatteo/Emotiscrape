import fileinput
import nltk

class Emotiscrape:

    def __init__(self):
        good_tweets = self.clean_tweets("good.txt")
        bad_tweets = self.clean_tweets("bad.txt")
        bag_of_emotions = ([(w, 'pos') for w in good_tweets] + [(w, 'neg') for w in bad_tweets])
        training_set = [(self.remove_features(w), c) for (w, c) in bag_of_emotions]
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)
        pass
        
    def clean_tweets(self, file, max=40000):
        word_bag = fileinput.input(file)
        tweets = []

        for words in word_bag:
            words_filtered = [e.lower().replace(",", "") for e in words.split() if len(e) > 3 and len(e) < 6]
            tweets.extend(words_filtered)

        tweets = tweets[:max]
        print "cleaned %s tweets from %s" % (len(tweets), file)
        return tweets


    def extract_features(self, document):
        document_words = set(document)
        features = {}
        for word in word_features:
          features['contains(%s)' % word] = (word in document_words)
        return features


    # return a frequency distribution (without the values)
    def get_word_features(self, wordlist):
        #contains key/val where val is the distro val
        wordlist = nltk.FreqDist(wordlist)
        # just want the words, not the count
        word_features = wordlist.keys()
        return word_features


    #document is a list of words to compare against the output of get_word_features()
    def extract_features(self, document):
        document_words = set(document)
        word_features = self.get_word_features(tweets)
        features = {}
        #print ">>>", document_words
        for word in word_features:
            s = 'contains(%s)' % str(word)
            features[s] = word in document_words
            #features['contains(%s)' % word] = (word in document_words)
            #print word in document_words
        return features


    # TODO: The reason that we compute the set of all words in a document in [3], rather than 
    # just checking if word in document, is that checking whether a word occurs in a set is much 
    # faster than checking whether it occurs in a list 
    def extract_features2(self, document):
        #document_words = set(document)
        word_features = self.get_word_features(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document)
        return features

    # Define a feature detector function.
    def document_features(self, document):
        #print document
        d = {}
        for word in document.split(" "):
            s = 'contains(%s)' % word
            d[s] = True
        return d
        #return dict([('contains(%s)' % w, True) for w in document])
        
    # TODO:
    # When working with large corpora, constructing a single list that contains the features of every instance can use up a large 
    # amount of memory. In these cases, use the function nltk.classify.apply_features, which returns an object that acts like a list 
    # but does not store all the feature sets in memory
    def remove_features(self, word):
        key = 'contains(%s)' % word
        return {key: True}


    def analyze_string(self, my_string):
       
        o = self.classifier.prob_classify(self.document_features(my_string))
        pos_score = o.prob("pos")
        neg_score = o.prob("neg")

        classification = self.classifier.classify(self.document_features(my_string))

        if pos_score >= neg_score:
            score = pos_score * 100
        else:
             score = neg_score * -100
        
        return [score, classification, my_string]



if __name__ == "__main__":

    emo = Emotiscrape()

    print "TEST MODE"
   
    
    test_samples = [
        'i love you harry!',
        'This is incredibly annoying, i hate working here and i hate this app',
        'You are a terrible person and everything you do is bad',
        'I love you all and you make me happy',
        'I frown whenever I see you in a poor state of mind',
        'Finally getting rich from my ideas. They make me smile.',
        'My mommy is poor',
        'I love butterflies. Yay for happy',
        'Everything is fail today and I hate stuff',
        'Larry is my friend, but boy is he shady',
    ]
    
    for sample in test_samples:
        o = emo.classifier.prob_classify(emo.document_features(sample))
        pos_score = o.prob("pos")
        neg_score = o.prob("neg")
        
        if pos_score >= neg_score:
            score = pos_score * 100
        else:
             score = neg_score * -100
             
       # print "neg", o.prob("neg")
       # print "pos", o.prob("pos")
        
        print "(%s) %s | %s" % (score, emo.classifier.classify(emo.document_features(sample)), sample)
        
        
# ?
# training_set = nltk.classify.apply_features(extract_features, tweets)

    










