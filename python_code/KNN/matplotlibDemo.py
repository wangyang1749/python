# import tkinter
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib as mpl

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# plt.switch_backend('agg')
plt.figure()
x=[0.2,0.4,0.8,1.2,1.6,2.0]
y=[0.026,0.078,0.160,0.216,0.314,0.363]
# plt.plot(x,y)
plt.scatter(x, y)
plt.plot(x, y,  'ko')
parameter = np.polyfit(x, y, n) # n=1为一次函数，返回函数参数
f = np.poly1d(parameter) # 拼接方程
plt.plot(x, f(x),"r--")

plt.show()