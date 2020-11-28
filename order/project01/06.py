import nltk
import string
import random

sw = set(nltk.corpus.stopwords.words('english'))
punctuation = set(string.punctuation)
def word_fratures(word):
    return {'len':len(word)}

def isStopword(word):
    return word in sw or word in punctuation

gb = nltk.corpus.gutenberg
# print(gb.fileids()[-5:])
words = gb.words("shakespeare-caesar.txt")
labeled_words = [(word.lower(),isStopword(word.lower()))
                for word in words]
# print(labeled_words)
random.seed(42)
random.shuffle(labeled_words)
featuresets = [(word_fratures(n),word) for (n, word) in labeled_words]
print(featuresets)

cutoff = int(.9*len(featuresets))
# print(cutoff)
tarin_set, test_set = featuresets[:cutoff], featuresets[cutoff:]

classifier = nltk.NaiveBayesClassifier.train(tarin_set)
print(classifier.classify(word_fratures('behold')))
print(classifier.classify(word_fratures('the')))

print(classifier.show_most_informative_features(5))