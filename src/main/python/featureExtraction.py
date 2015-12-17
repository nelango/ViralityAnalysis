import string
from nltk.corpus import stopwords
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


s = "It was November. Although it was not yet late, the sky was dark when I turned into Laundress Passage. Father had finished for the day, switched off the shop lights and closed the shutters; but so I would not come home to darkness he had left on the light over the stairs to the flat. Through the glass in the door it cast a foolscap rectangle of paleness onto the wet pavement, and it was while I was standing in that rectangle, about to turn my key in the door, that I first saw the letter. Another white rectangle, it was on the fifth step from the bottom, where I couldn't miss it."
# number of tokens
tokens = s.split()
no_tokens = len(tokens)

# avg token length
count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
s_chars =  count(s, string.ascii_letters)
# s_punct = count(s, string.punctuation)
avg_token_length = s_chars/no_tokens

# number of unique tokens
unique_tokens = set(tokens)
no_unique_tokes = len(unique_tokens)

# number of non-stop words
stop = stopwords.words('english')
non_stopwords = [i for i in tokens if i not in stop]
no_non_stopwords = len(non_stopwords)

# sentiment analysis - polarity and subjectivity
blob = TextBlob(s)
# blob.tags
# blob.noun_phrases 
# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity)
content_polarity = blob.sentiment.polarity
content_subjectivity = blob.sentiment.subjectivity

# rate of positivity and negativity
s_analyzer = TextBlob(s, analyzer=NaiveBayesAnalyzer())
# classification = s_analyzer.sentiment.classification
p_pos = s_analyzer.sentiment.p_pos
p_neg = s_analyzer.sentiment.p_neg
print p_pos, p_neg




