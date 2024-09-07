import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a.argmax(axis=0))

# Output:
# [2 3 4]

# Explanation:
# The maximum element along axis 0 is at index 2.
# The maximum element along axis 1 is at index 3.
# The maximum element along axis 2