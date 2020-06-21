import nltk
import string
sw = set(nltk.corpus.stopwords.words('english'))
gb = nltk.corpus.gutenberg
text_sent =  gb.sents("milton-paradise.txt")[:2]
punctuation = set(string.punctuation)
for sent in text_sent:
    filtered = [w.lower() for w in sent if w.lower() not in sw 
            and w.lower() not in punctuation]
    print(type(filtered))
    fd = nltk.FreqDist(filtered)
    print(fd.keys())
    print(fd.values())