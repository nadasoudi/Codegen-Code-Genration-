import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.concatenate((a, b), axis=0)
print(c)

d = np.concatenate((a, b), axis=1)
print(d)

# Output:
[[1 2]