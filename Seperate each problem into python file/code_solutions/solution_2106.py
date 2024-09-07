import numpy as np

def median(arr):
    arr = np.array(arr)
    arr = arr.flatten()
    arr = np.sort(arr)
    return arr[len(arr)//2]

print(median([1,2,3,4,5,6,7,8,9,10]))

"""

# Solution

import numpy as np

def median(arr):
    arr = np.array(arr)
    arr =