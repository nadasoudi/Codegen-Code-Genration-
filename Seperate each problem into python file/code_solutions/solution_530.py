import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

np.savez('arr1.npz', arr1)
arr2 = np.load('arr1.npz')

arr3 = arr2['arr1']
arr4 = arr2['arr2']

arr3 = arr3.