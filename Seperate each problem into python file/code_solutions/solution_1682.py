import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

if a[0, 0] == 1:
    print("Row 0 contains 1")
else:
    print("Row 0 does not contain 1")

if a[1, 0] == 2:
    print("Row 1 contains 2")
else:
    print("Row 1 does not contain 2")

if a[0, 1] == 3:
    print("Row 0