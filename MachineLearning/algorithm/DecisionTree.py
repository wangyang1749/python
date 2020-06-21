from math import log
import operator

# 计算香农熵
def calcSchannonEnt(dataset):
    numEntrise = len(dataset) # 5
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1] # yes
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1
    # {'no': 3, 'yes': 2}
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntrise
        shannonEnt -=prob*log(prob,2)
    return shannonEnt

def createDataset():
    dataset = [[1,1,'yes'],
                [1,1,'yes'],
                [1,0,'no'],
                [0,1,'no'],
                [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataset,labels

myData,labels = createDataset()
# res = calcSchannonEnt(myData)
# print(res)

# dataset
def splitDataset(dataset,axis,value):
    retDataset = [] 
    for featVet in dataset:
        if featVet[axis] == value:
            reducedFeatVec = featVet[:axis]
            reducedFeatVec.extend(featVet[axis+1:])
            retDataset.append(reducedFeatVec)
    return retDataset


# res = splitDataset(myData,0,1)
# print(res) # [[1, 'yes'], [1, 'yes'], [0, 'no']]

def chooseBestFeatureToSplit(dataset):
    numFeature = len(dataset[0])-1 # 2
    baseEntropy = calcSchannonEnt(dataset)
    baseInfoGain = 0.0; baseFeature = -1
    for i in range(numFeature):
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataset = splitDataset(dataset,i,value)
            prob = len(subDataset)/float(len(dataset))
            newEntropy += prob * calcSchannonEnt(subDataset)
        infoGain = baseEntropy - newEntropy
        if(infoGain>baseInfoGain):
            baseInfoGain=infoGain
            baseFeature = i
    return baseFeature

# res = chooseBestFeatureToSplit(myData)
# print(res)

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys() : classCount[vote] = 0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.iteritems()
            ,key=operator.itemgetter(1),reversed=True)
    return sortedClassCount[0][0]


def createTree(dataset,labels):
    classList = [example[-1] for example in dataset]
    # 计算类别次数
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataset]
    uniqueValues = set(featValues)
    for value in uniqueValues:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(
            splitDataset(dataset,bestFeat,value),subLabels)
    return myTree

res =  createTree(myData,labels)
print(res)

# 使用决策树执行分类算法
def classify(inputTree,featLabels,testVec):
    firstStr = list(inputTree.keys())[0]
    # print(firstStr[0])
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__=='dict':
                classLabel = classify(secondDict[key],
                    featLabels,testVec)
            else:   
                classLabel = secondDict[key]
    return classLabel

# myTree =  createTree(myData,labels)
# print(myTree)
# res = classify(myTree, ['no surfacing','flippers'],[1,0])
# print(res)