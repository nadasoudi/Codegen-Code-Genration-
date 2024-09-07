import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr)

# Replace all numbers in array which is equal to given number

arr[arr == 5] = 0

print(arr)

# Replace all numbers in array which is less than given number

arr[arr < 5] = 0

print(arr)

#