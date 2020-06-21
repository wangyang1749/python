import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('numpy/01.jpg')

img_arr = np.array(img)
acopy = img_arr.copy()
aview = img_arr.view()


def shuffle_indices(size):
    arr = np.arange(size)
    np.random.shuffle(arr)
    return arr


def get_indices(size):
    arr = np.arange(size)
    return arr % 4 ==0




    
