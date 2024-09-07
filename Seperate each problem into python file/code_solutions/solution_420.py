import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

c = a.copy()
d = b.copy()

c[0, 0] = 100
d[0, 0] = 100

print(a)
print(b)
print(c)
print(d)

# Output: