import numpy as np

a = np.arange(24).reshape(2,3,4)
print(a.ravel()) # 将函数[拆解]为一维数组
print(a.flatten()) # 数组拉直
a.transpose() # 转置
a.shape=(6,4) # 改变a的形状
a.reshape(4,6)
print(a)
a.resize(4,6)
print(a)



