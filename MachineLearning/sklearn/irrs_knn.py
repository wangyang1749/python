from sklearn import datasets
from KnnMethod import classify0

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# 预测向量[0.2,0.4] 所在的分类    
result=classify0([5.8, 2.7, 5.1 ,1.9],iris_X,iris_y,3)
print(result)
