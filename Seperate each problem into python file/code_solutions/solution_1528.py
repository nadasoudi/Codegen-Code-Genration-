import numpy as np

arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]])

print(arr[arr > 5])

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [10, 9