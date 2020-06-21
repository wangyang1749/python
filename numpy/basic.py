import numpy as np

# 创建数组
a = np.array([1,2,3,4])
print(type(a)) # <class 'numpy.ndarray'>
a = np.arange(9)
print(type(a)) # <class 'numpy.ndarray'>

# 一维数组切片
print(a) # [0 1 2 3 4 5 6 7 8]
print(a[:5]) # [0 1 2 3 4] 小于5的数
print(a[5:]) # [5 6 7 8] 大于等于5的数
print(a[2:7]) # [2 3 4 5 6]
print(a[::-1]) # [8 7 6 5 4 3 2 1 0]
print(a[:8:2]) #[0 2 4 6]



