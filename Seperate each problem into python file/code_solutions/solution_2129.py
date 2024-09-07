import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

# Add the polynomial to the solution
x = np.append(x, y)

# Print the solution
print(x)

# Add another polynomial to the solution
x = np.append(x, y, axis=0)

# Print the solution
print(x)

# Add