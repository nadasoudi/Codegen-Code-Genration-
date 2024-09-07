import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if np.nonzero(a)[0].size!= 0:
    print("Array contains non-zero elements.")
else:
    print("Array does not contain non-zero elements.")

# Output:
# Array contains non-zero elements.
# 
# Array does not contain non-zero elements.