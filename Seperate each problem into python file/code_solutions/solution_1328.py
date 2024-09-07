import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

zero_indices = np.where(arr == 0)

print(zero_indices)

# Output:
# array([0, 1, 3, 4, 6, 7, 8, 9, 10])

# In[ ]: