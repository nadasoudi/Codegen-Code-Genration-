import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4, 5])
c = np.array([1, 2, 3, 4, 5])

print(np.all(a == b))
print(np.all(a == c))

# Output:
# True
# True