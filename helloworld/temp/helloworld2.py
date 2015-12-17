import sys
sys.path.insert(0, 'lib')
import webapp2
import string
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from collections import Counter

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        n = self.compute()
        self.response.write(n)

    # def post(self):
    #     name = self.request.get("name")
    #     self.response.headers['Content-Type'] = 'text/plain'
    #     n = self.compute()
    #     self.response.write(n)

    def readwords(self, filename):
    	f = open(filename)
    	words = [ line.rstrip() for line in f.readlines()]
    	return words

    def compute(self):
    	title = "Why November is dark and horrible"
    	s = "It was November. Although it was not yet late, the sky was dark when I turned into Laundress Passage. Father had finished for the day, switched off the shop lights and closed the shutters; but so I would not come home to darkness he had left on the light over the stairs to the flat. Through the glass in the door it cast a foolscap rectangle of paleness onto the wet pavement, and it was while I was standing in that rectangle, about to turn my key in the door, that I first saw the letter. Another white rectangle, it was on the fifth step from the bottom, where I couldn't miss it."
    	tokens = s.split()
        # number of tokens
    	 = len(tokens)
    	
    	blob = TextBlob(s)
    	global_sentiment_polarity = blob.sentiment.polarity
    	global_subjectivity = blob.sentiment.subjectivity
    	
    	positive = self.readwords('positive.txt')
    	negative = self.readwords('negative.txt')
    	count = Counter(s.split())
    	pos = 0
    	neg = 0
    	for key, val in count.iteritems():
    		key = key.rstrip('.,?!\n') # removing possible punctuation signs
    		if key in positive:
    			pos = pos + 1
    		if key in negative:
    			neg = neg + 1
    	non_neutral_tokens = pos+neg
    	rate_positive_words = float(pos)/float(non_neutral_tokens)
    	rate_negative_words = float(neg)/float(non_neutral_tokens)
    	p_pos = float(pos)/float(n)
    	p_neg = float(neg)/float(n)
    	
    	blob = TextBlob(title)
    	title_polarity = blob.sentiment.polarity
    	title_subjectivity = blob.sentiment.subjectivity

    	stop_words = self.readwords('stopwords.txt')
    	n_stop_words = 0
    	count = Counter(s.split())
    	for key, val in count.iteritems():
    		key = key.rstrip('.,?!\n') # removing possible punctuation signs
    		if key in stop_words:
    			n_stop_words = n_stop_words + 1
    	n_non_stop_words = n - n_stop_words
    	return (n_non_stop_words)


app = webapp2.WSGIApplication([
                               ('/hello', MainPage),
                               ], debug=True)