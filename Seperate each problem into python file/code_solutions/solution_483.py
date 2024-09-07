import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr[:,1] = arr[:,4]
arr[:,2] = arr[:,5]
arr[:,3] = arr[:,6]
arr[:,4] = arr[:,1]
arr[:,5] = arr[:,2]
arr[:,6]