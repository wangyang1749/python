from numpy import *
import operator

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=["A","A","B","B"]
    return group,labels
group,labels=createDataSet()
# print(group,labels)

#使用K邻近算法处理数据
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    # print(dataSetSize)
#1、计算已知类别数据集中的点与当前点之间的距离
    diffMat=tile(inX,(dataSetSize,1))#将inX变为1行4列的矩阵
    diffMat=diffMat-dataSet
    # print(diffMat)
    sqDiffMat=diffMat**2
    # print(sqDiffMat)
    sqDistances=sqDiffMat.sum(axis=1)
    # print(sqDistances)
    distance=sqDistances**0.5
    print("distance is:",distance)
#2、按照距离递增次序排序,返回数组从小到大的索引
    sortedDistIndicies=distance.argsort()
    print("argsort is:",sortedDistIndicies)
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        # print(voteIlabel)
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        # print(classCount)
    # print(classCount)
    sortedClassCount = sorted(classCount.items(),key=lambda item: item[1],reverse=True)
    # print(sortedClassCount)
    return sortedClassCount[0][0]
#3、选取与当前点距离最小的k个点
#4、确定前k个点所在类别出现频率
#5、返回前k个点出现频率最高的类别作为当前点的预测分类

result=classify0([0,0],group,labels,3)
print(result)