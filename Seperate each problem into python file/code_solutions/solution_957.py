import numpy as np

arr = np.array([[1,2,3,4,5,6,7,8,9,10],
                [10,9,8,7,6,5,4,3,2,1]])

arr.sort()
print(arr)

arr.sort(axis=0)
print(arr)

arr.sort(axis=1)
print(arr)

arr.sort(axis=0,kind='quicksort')