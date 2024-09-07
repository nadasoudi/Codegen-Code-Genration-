import numpy as np

def percentile(arr, per):
    arr = np.asarray(arr)
    arr = arr.astype(np.float64)
    arr = np.sort(arr)
    arr = arr[::-1]
    arr = arr[:per]
    return arr

print(percentile([1,2,3,4,5,6,7,8,9,10], 10))

"""

# %%