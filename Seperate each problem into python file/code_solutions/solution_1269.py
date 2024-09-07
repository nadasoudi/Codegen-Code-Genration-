import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(a.shape)
print(b.shape)

if a.shape == b.shape:
    print("Both arrays have same dimensions")
else:
    print("Both arrays have different dimensions")

# Output:
# (2