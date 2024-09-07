import numpy as np

x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(x.mean(axis=0))

# Output:
# [2.5 3.5 4.5 5.5]

# Hint: To calculate mean across the rows, use np.mean(x, axis=0).

# Hint: To calculate mean across the columns, use np.