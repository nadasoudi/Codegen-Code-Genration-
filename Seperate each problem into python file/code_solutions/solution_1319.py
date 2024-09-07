import numpy as np

arr = np.array([1, 2, 3, 4, 5])

np.savetxt('arr.txt', arr)

arr2 = np.loadtxt('arr.txt')

print(arr2)

arr3 = np.loadtxt('arr.txt', dtype=int)

print(arr3)

arr4 = np.loadtxt('arr.txt', dtype=str)

print(arr4)