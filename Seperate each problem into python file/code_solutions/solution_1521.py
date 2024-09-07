import numpy as np

# Create an array of random numbers between 0 and 1
np.random.seed(0)
x = np.random.uniform(0, 1, size=40)

# Create a one dimensional array of forty pseudo-randomly generated values
y = np.zeros(40)
for i in range(40):
    y[i] = x[i]

# Display the