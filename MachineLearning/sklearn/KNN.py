from numpy import *
import matplotlib.pyplot as plt
from sklearn import datasets

# def createDataSet():
#     group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
#     labels=["A","A","B","B"]
#     return group,labels
# group,labels=createDataSet()

iris = datasets.load_iris()
group = iris.data
labels = iris.target
target = iris.feature_names


# 使用K邻近算需要4个参数：
# inX 需要预测分类向量
# dataSet 训练样本数据集
# labels 训练样本对应的标签
# k 选择最邻近的数目                   
def classify0(inX,dataSet,labels,k):
    # 获得训练样本的个数，本例中有4个
    dataSetSize=dataSet.shape[0] # 4
    # 复制inX，为4行1列
    diffMat=tile(inX,(dataSetSize,1))
    '''
    [[0.2 0.4]
     [0.2 0.4]
     [0.2 0.4]
     [0.2 0.4]]
    '''
    # 计算两点之差
    diffMat=diffMat-dataSet
    '''
    [[-0.8 -0.7]
     [-0.8 -0.6]
     [ 0.2  0.4]
     [ 0.2  0.3]]
    '''
    # 计算平方和
    sqDiffMat=diffMat**2
    '''
    [[0.64 0.49]
     [0.64 0.36]
     [0.04 0.16]
     [0.04 0.09]]
    '''
    # 相加
    sqDistances=sqDiffMat.sum(axis=1)
    '''
    [1.13 1.   0.2  0.13]
    '''
    # 开放
    distance=sqDistances**0.5
    '''
    [1.06301458 1.         0.4472136  0.36055513]
    '''
    # 升序排序，返回的是数组下标
    sortedDistIndicies=distance.argsort()
    '''
    [3 2 1 0] 数组下标为0的元素最大
    '''
    classCount={} # {'B': 2, 'A': 1}
    for i in range(k):
        # 循环k次，获取升序排列的第i个标签
        voteIlabel=labels[sortedDistIndicies[i]] # B B A
        # 计算在循环的k次中，某一个标签出现的次数
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
        ''' k = 3
        {'B': 1} 第一次循环
        {'B': 2} 第二次循环
        {'B': 2, 'A': 1} 第三次循环，A出现1次，B出现2次
        '''
    # 降序排列得到的字典的值
    sortedClassCount = sorted(classCount.items(),key=lambda item: item[1],reverse=True)
    '''
    [('B', 2), ('A', 1)]
    '''
    return sortedClassCount[0][0]

print(target)
# 预测向量[0.2,0.4] 所在的分类    
result=classify0([5.8, 2.7, 5.1 ,1.9],group,labels,3)
print(result)