
'''
计算 1^2+ 2^2+ ... + n^2 + 1^3+2^3+...+n^3
'''

import numpy as np
def numpy_sum(n):
    a = np.arange(n)**2
    b = np.arange(n)**3
    c = a+b
    return c

print(numpy_sum(5))
# ---arange 范围
a = np.arange(5)
print(a.dtype)
print(type(a)) # <class 'numpy.ndarray'>

# ---shape 形状
print("shape---",a.shape) # (5,) 五行1列
a = np.array([[1,2,3],[3,4,5]])
print("array---",a.shape) #  (2, 3) 两行三列

# --- np.array
b = np.array(10)
print(b.dtype)
print(type(b)) # <class 'numpy.ndarray'>
a = np.array([np.arange(5),np.arange(5)])
print(a.dtype.itemsize)

# ---dtype
print(np.dtype('d'))

# ---数组的切片
a = np.arange(9)
print(a)
print(a[3:7])
print(a[:7:2])
print(a[::-1])

# ---处理数组形状
a = np.arange(24).reshape(2,3,4)
print(a)
print(a.shape)
