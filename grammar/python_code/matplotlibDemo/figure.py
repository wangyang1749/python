import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

# 第一张图
# plt.figure()
# plt.plot(x,y1)

# 第二张图,一个figure可以画多条线
plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color="red",linewidth="1.0",linestyle="--")
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel("xxx")
plt.ylabel("yyy")

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8],["aaa","bbb"])

plt.show()