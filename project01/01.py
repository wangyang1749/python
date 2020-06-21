import nltk
sw = set(nltk.corpus.stopwords.words('english'))
# print(sw)
gb = nltk.corpus.gutenberg
print(gb.fileids()[-5:])
text_sent =  gb.sents("milton-paradise.txt")[:2]
print(text_sent)

print("---------")
for sent in text_sent:
    filtered = [w for w in sent if w.lower() not in sw]
    print(filtered)
    print("===")
    tagged = nltk.pos_tag(filtered)
    print(tagged)