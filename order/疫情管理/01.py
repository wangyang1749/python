import numpy as np
import matplotlib.pyplot as plt

# x = [1,2]  #横坐标
# y = [3,4]  #第一个纵坐标
# y1 = [5,6]  #第二个纵坐标

# x = np.arange(len(x)) #首先用第一个的长度作为横坐标
# width = 0.05  #设置柱与柱之间的宽度
# fig,ax = plt.subplots()
# ax.bar(x,y,width,alpha = 0.9)
# ax.bar(x+width,y1,width,alpha = 0.9,color= 'red')
# ax.set_xticks(x +width/2)#将坐标设置在指定位置
# ax.set_xticklabels(x)#将横坐标替换成
# plt.show()


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]

bar_width = 0.35
tick_label = ["A", "B", "C", "D", "E"]

plt.bar(x, y, bar_width, align="center", color="c", label="班级A", alpha=0.5)
plt.bar(x+bar_width, y1, bar_width, color="b", align="center", label="班级", alpha=0.5)

plt.xlabel("测试难度")
plt.ylabel("试卷份数")

plt.xticks(x+bar_width/2, tick_label)

plt.legend()

plt.show()