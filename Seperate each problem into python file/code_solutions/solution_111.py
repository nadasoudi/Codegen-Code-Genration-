import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr.sort()

print(arr)

arr.sort(reverse=True)

print(arr)

arr.sort()

print(arr)

arr.sort(key=lambda x: x % 2)

print(arr)

arr.sort(key=lambda x: x % 2