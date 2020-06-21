# 鸢尾花分类
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# print(iris.feature_names)
# print(iris_X[:2,:])
# print(iris_y)

X_train,X_test,y_train,y_test = train_test_split(iris_X,iris_y,test_size=0.3)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
# 预测[5.8, 2.7, 5.1 ,1.9]
print(knn.predict([[5.8, 2.7, 5.1 ,1.9]]))
print(knn.predict(X_test))
print(y_test)
