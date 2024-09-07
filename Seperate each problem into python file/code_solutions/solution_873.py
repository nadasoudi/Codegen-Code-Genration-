import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

arr3 = np.vstack((arr1, arr2))

print(arr3)

arr4 = np.hstack((arr1, arr2))

print(arr4)

arr5 = np.dstack((arr1, arr2))

print(arr5)

arr6