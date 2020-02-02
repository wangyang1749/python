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
