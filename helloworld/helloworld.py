"""This is the homerwork for CS8803 ASE 
implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""
import sys
sys.path.insert(0, 'lib')
import webapp2
import string
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from collections import Counter

import endpoints
import json
from protorpc import messages
from protorpc import message_types
from protorpc import remote
import time
import urllib2
from google.appengine.api import mail

# import pandas as pd
import numpy as np
import csv
# # import os
# # # import math
# # from sklearn import datasets
# # from sklearn import datasets
# # from sklearn import metrics
# # from sklearn.ensemble import RandomForestRegressor
# # from sklearn.cross_validation import cross_val_score
# # from sklearn.cross_validation import train_test_split
# from sklearn.preprocessing import normalize

package = 'Hello'

class KNNLearner:
    def __init__(self, k=3):
        self.k = k
        self.Xtrain = []
        self.Ytrain = []

    def addEvidence(self, Xtrain, Ytrain):
      self.Xtrain = Xtrain
      self.Ytrain = Ytrain

    def query(self, Xtest):
      train = np.c_[self.Xtrain, self.Ytrain]
      delta = []
      for j in range(train.shape[0]):
        dist = 0
        for i in range(len(Xtest)):
          dist = dist + (train[j][i] - Xtest[i])**2
        dist = np.sqrt(dist)
        delta.append(dist)
      delta = np.c_[delta, train]
      delta = delta[delta[:,0].argsort()]
      delta = delta[0:self.k]
      Ytest = delta[:,-1].mean()
      return Ytest

class Input(messages.Message):
  titleName = messages.StringField(1, required = True)
  linksNumber = messages.IntegerField(2, required = True)
  imagesNumber = messages.IntegerField(3, required = True)
  videosNumber = messages.IntegerField(4, required = True)
  keywords = messages.IntegerField(5, required = True)
  articleContent = messages.StringField(6, required = True)
  day = messages.StringField(7, required = True)
  category = messages.StringField(8, required = True)



class Output(messages.Message):
  """shares and sentiment."""
  shares = messages.IntegerField(1)
  contentSubjectivity = messages.FloatField(2)
  contentSentimentPolarity = messages.FloatField(3)
  contentPositiveRate = messages.FloatField(4)
  contentNegativeRate = messages.FloatField(5)
  titleSubjectivity = messages.FloatField(6)
  titlePolarity = messages.FloatField(7)

@endpoints.api(name='prediction', version='v1')
class PredictorApi(remote.Service):
  """Predictor API v1."""

  # @endpoints.method(message_types.VoidMessage, Output,
  #                   path='prediction', http_method='GET',
  #                   name='getting.tuple')
  # def give_output(self, unused_request):
  #   return Output(shares=5) 

  @endpoints.method(Input, Output,
                  path='prediction', http_method='POST',
                  name='sending.shares')
  def take_input(self, request):
    # n = self.compute(request)
    n_tokens_title, n_tokens_content, n_unique_tokens,n_non_stop_words, n_non_stop_unique_tokens, average_token_length, global_subjectivity, global_sentiment_polarity,global_rate_positive_words, global_rate_negative_words, rate_positive_words, rate_negative_words, title_subjectivity,title_polarity = self.compute(request)
    testX = [n_tokens_title, n_tokens_content, n_unique_tokens,n_non_stop_words, n_non_stop_unique_tokens]
    linksNumber = request.linksNumber
    imagesNumber = request.imagesNumber
    videosNumber = request.videosNumber
    keywords = request.keywords
    day = request.day
    category = request.category

    testX = testX + [linksNumber,imagesNumber,videosNumber,average_token_length,keywords]

    day_list = []
    if day=="Monday":
      day_list = [1,0,0,0,0,0,0,0]
    elif day=="Tuesday":
      day_list = [0,1,0,0,0,0,0,0]
    elif day=="Wednesday":
      day_list = [0,0,1,0,0,0,0,0]
    elif day=="Thursday":
      day_list = [0,0,0,1,0,0,0,0]
    elif day=="Friday":
      day_list = [0,0,0,0,1,0,0,0]
    elif day=="Saturday":
      day_list = [0,0,0,0,0,1,0,1]
    elif day=="Sunday":
      day_list = [0,0,0,0,0,0,1,1]


    cat_list = []
    if category=="Lifestyle":
      cat_list = [1,0,0,0,0,0]
    elif category=="Entertainment":
      cat_list = [0,1,0,0,0,0]
    elif category=="Business":
      cat_list = [0,0,1,0,0,0]
    elif category=="Social Media":
      cat_list = [0,0,0,1,0,0]
    elif category=="Tech":
      cat_list = [0,0,0,0,1,0]
    elif category=="World":
      cat_list = [0,0,0,0,0,1]

    testX = testX + cat_list
    testX = testX + day_list
    testX = testX + [global_subjectivity, global_sentiment_polarity,global_rate_positive_words, global_rate_negative_words, rate_positive_words, rate_negative_words, title_subjectivity,title_polarity]
    n = int(self.testLearner(testX))
    return Output(shares=n, contentSubjectivity=global_subjectivity,contentSentimentPolarity= global_sentiment_polarity,contentPositiveRate=global_rate_positive_words, contentNegativeRate=global_rate_negative_words, titleSubjectivity=title_subjectivity,titlePolarity=title_polarity)

  def readwords(self, filename):
    f = open(filename)
    words = [ line.rstrip() for line in f.readlines()]
    return words

  def testLearner(self, testX):
    # my_data = np.genfromtxt('data4.csv', delimiter=',')
    # fileReader = csv.reader(csv_file.split("\n"))
    # testX = np.array(testX)
    with open("OnlinePopularityAnalysis.csv", 'r') as f:
      data = [row for row in csv.reader(f.read().splitlines())]
    data = np.array(data)
    data = data[1:,[1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,30,31,32,33,34,35,36,37,43,44,45,46,47,48,55,56,59]]
    data = data.astype(np.float)
    X = data[:,0:-1]
    trainX = data[:-1,0:-1]
    trainY = data[:-1,-1]
    learner = KNNLearner(k = 3) # constructor
    # testX = data[-1,1:-1]
    learner.addEvidence(trainX, trainY) # training step
    predY = learner.query(testX) # get the predictions
    return int(predY)

  def non_stop_words(self,n,s):
    stop_words = self.readwords('stopwords.txt')
    n_stop_words = 0
    count = Counter(s.split())
    for key, val in count.iteritems():
      key = key.rstrip('.,?!\n') # removing possible punctuation signs
      if key in stop_words:
        n_stop_words = n_stop_words + 1
    n_non_stop_words = n - n_stop_words
    return (n_non_stop_words)

  def non_stop_unique_tokens(self,n,s):
    stop_words = self.readwords('stopwords.txt')
    n_stop_unique_tokens = 0
    for key in s:
      if key in stop_words:
        n_stop_unique_tokens = n_stop_unique_tokens + 1
    n_non_stop_unique_tokens = n - n_stop_unique_tokens
    return (n_non_stop_unique_tokens)
  
  def sentiment_analysis(self,s,n_tokens_content):
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
    global_rate_positive_words = float(pos)/float(n_tokens_content)
    global_rate_negative_words = float(neg)/float(n_tokens_content)
    if non_neutral_tokens>0:
      rate_positive_words = float(pos)/float(non_neutral_tokens)
      rate_negative_words = float(neg)/float(non_neutral_tokens)
    else:
      rate_positive_words = 0
      rate_negative_words = 0
    return (global_rate_positive_words,global_rate_negative_words,rate_positive_words,rate_negative_words)


  def compute(self,request):
      title = request.titleName
      n_tokens_title = len(title)
      s=request.articleContent
      # s = "It was November. Although it was not yet late, the sky was dark when I turned into Laundress Passage. Father had finished for the day, switched off the shop lights and closed the shutters; but so I would not come home to darkness he had left on the light over the stairs to the flat. Through the glass in the door it cast a foolscap rectangle of paleness onto the wet pavement, and it was while I was standing in that rectangle, about to turn my key in the door, that I first saw the letter. Another white rectangle, it was on the fifth step from the bottom, where I couldn't miss it."
      # number of tokens in content
      tokens = s.split()
      n_tokens_content = len(tokens)

      # number of unique tokens
      unique_tokens = set(tokens)
      n_unique_tokens = len(unique_tokens)

      # number of non-stop words
      n_non_stop_words = self.non_stop_words(n_tokens_content,s)

      # number of non-stop unique tokens
      n_non_stop_unique_tokens = self.non_stop_unique_tokens(n_unique_tokens,unique_tokens)

      #average token length
      count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
      s_chars =  count(s, string.ascii_letters)
      average_token_length = s_chars/n_tokens_content
      
      # content polarity and subjectivity
      blob = TextBlob(s)
      global_sentiment_polarity = blob.sentiment.polarity
      global_subjectivity = blob.sentiment.subjectivity
      
      #rate of positivity and negativity
      global_rate_positive_words, global_rate_negative_words, rate_positive_words, rate_negative_words = self.sentiment_analysis(s,n_tokens_content)
      
      # title polarity and subjectivity
      blob = TextBlob(title)
      title_polarity = blob.sentiment.polarity
      title_subjectivity = blob.sentiment.subjectivity
      return(n_tokens_title, n_tokens_content, n_unique_tokens,n_non_stop_words, n_non_stop_unique_tokens, average_token_length, global_subjectivity, global_sentiment_polarity,global_rate_positive_words, global_rate_negative_words, rate_positive_words, rate_negative_words, title_subjectivity,title_polarity)

    # return Input(titleName=request.titleName, imagesNumber=request.imagesNumber, videosNumber=request.videosNumber,
    #   keywords=request.keywords, articleContent=request.articleContent, day=request.day, category=request.category)
   
APPLICATION = endpoints.api_server([PredictorApi])