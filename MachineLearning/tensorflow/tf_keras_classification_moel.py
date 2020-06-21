import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time
import tensorflow as tf
from tensorflow import keras

# print(tf.__version__)
print(sys.version_info)
for module in mpl,np,tf:
    print(module.__name__,module.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(x_train_all,y_tarin_all),(x_test,y_test) = fashion_mnist.load_data()
x_valid,x_train = x_train_all[:5000],x_train_all[5000:]
y_vaild,y_tarin = y_tarin_all[:5000],y_tarin_all[5000:]

print(x_test.shape,y_test.shape)
print(x_valid.shape,x_valid.shape)
print(x_train.shape,y_tarin.shape)


def show_imshow_image(img_arr):
    plt.imshow(img_arr,cmap="binary")
    plt.show()

# show_imshow_image(x_train[0])

# 显示n行n列,in x_data y_data lable 名称
def show_image(n_rows,n_cols,x_data,y_data,class_name):
    assert len(x_data) == len(y_data)
    # 行和列的乘积不能大于样本数
    assert n_rows * n_rows<len(x_data)
    # 定义一张大图
    plt.figure(figsize=(n_cols*1.4,n_rows*1.6))
    for row in range(n_rows):
        for col in range(n_cols):
            # 当前位置图片的索引
            index = n_cols * row + col
            plt.subplot(n_rows,n_cols,index+1)
            plt.imshow(x_data[index],cmap="binary",
                        interpolation="nearest")
            plt.axis('off') # 关闭坐标系
            plt.title(class_name[y_data[index]])
    plt.show()

class_name=['T-shirt','Trouser','Pullover',
            'Dress','Coat','Sandal','Shirt',
            'Sneaker','Bag','Ankle boot']

show_image(3,5,x_train,y_tarin,class_name)

    
