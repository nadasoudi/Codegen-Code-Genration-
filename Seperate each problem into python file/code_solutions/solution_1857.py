import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[-1, 2, -3], [4, 5, 6]])

print(np.negative(x))
print(np.negative(y))

# Output:
[[-1 -1 -1]
 [-1 -1 -1]
 [-1 -1 -1]]

# Output:
[[-1 -1]
 [-1 -1]
 [-