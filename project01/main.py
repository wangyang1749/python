
include = ["the"]

def wordCount(content):
    wordArr = content.split()
    counts = {}
    for word in wordArr:
        if word in include:
            counts[word] = counts.get(word, 0) + 1
    countsList = list(counts.items())
    countsList.sort(key=lambda x:x[1], reverse=True)
    return countsList

with open("vocabulary/EnglishText.txt","r") as inputFile:
    print(wordCount(inputFile.read()))
