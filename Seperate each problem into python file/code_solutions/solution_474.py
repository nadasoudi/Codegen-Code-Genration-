import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

if arr[0, 0] == 1:
    print("Row 0 contains 1")
else:
    print("Row 0 does not contain 1")

if arr[1, 1] == 2:
    print("Row 1 contains 2")
else:
    print("Row 1 does not contain 2")

if arr[