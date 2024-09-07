import numpy as np

# Create a random array of 1000 elements
np.random.seed(0)
a = np.random.randint(0, 100, 1000)

# Compute the average
avg = np.mean(a)

# Compute the variance
var = np.var(a)

# Compute the standard deviation
std = np.std(a)

# Print the results
print("The