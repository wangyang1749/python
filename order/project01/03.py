import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy
import string

labeled_docs = [(list(movie_reviews.words(fid)),cat)
for cat in movie_reviews.categories()
for fid in movie_reviews.fileids(cat)]

print(labeled_docs)