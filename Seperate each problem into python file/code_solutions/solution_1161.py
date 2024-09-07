import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(np.mean(a, axis=0))
print(np.mean(b, axis=0))

# Output:
# [7.5 6.5]
# [10.5 11.5]

# H