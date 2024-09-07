import numpy as np

arr = np.array(['a', 'b', 'c', 'd', 'e', 'f'])

arr = np.append(arr, np.zeros(3))

print(arr)

arr = np.append(arr, np.zeros(3), axis=0)

print(arr)

arr = np.append(arr, np.zeros(3), axis=1)