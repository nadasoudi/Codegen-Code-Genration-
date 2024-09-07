import numpy as np

a = np.arange(300).reshape(300,400,5)
b = np.arange(400).reshape(300,400,5)

a[:,:,0] = 255
a[:,:,1] = 255
a[:,:,2] = 255
a