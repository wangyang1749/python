import numpy as np

arr=[1,2,3,4,5]
# 求平均值
print(np.mean(arr))
# 方差
print(np.var(arr,ddof=1))
# 标准差
print(np.std(arr,ddof=1))

t1 = np.var(arr,ddof=1)
print(int(t1))
print(type(t1))
a=np.array([1,2])
print(a**2)