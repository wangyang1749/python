import numpy as np

a = np.arange(9).reshape(3,3)
b = 2*a
np.hstack((a,b)) # horizontal stack
np.concatenate((a,b),axis=1) 
np.vstack((a,b)) # vertical stack
np.concatenate((a,b),axis=0)
np.dstack((a,b))# deep stack