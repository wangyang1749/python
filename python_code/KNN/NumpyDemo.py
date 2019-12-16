from numpy import *

a1 = array([1,5,9,4])
print(type(a1))
a2=a1.argsort()
print(a1)
print(a2)
print(type(a2))
print(a1[a2[0]])