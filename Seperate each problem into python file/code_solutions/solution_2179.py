import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

a[0, 1] = 7
a[1, 0] = 8

print(a)

# Output:
# [[1 7]
#  [4 5]
#  [8 6]]

# a[0, 1] = 7
# a[1, 0] = 8

# Output:
# [[1 7]
#