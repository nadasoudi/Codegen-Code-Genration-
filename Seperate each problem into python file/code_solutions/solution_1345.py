import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a.floor())
print(a.ceiling())
print(a.trunc())

# Output:
# [1 2 3 4 5 6 7 8 9]
# [1 2 3 4]
# [1 2 3 4 5 6 7 8 9]
# [1 2 3 4]