import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('covariance.txt', delimiter=',')

# Create a correlation matrix
corr = np.corrcoef(data[0], data[1])

# Plot the correlation matrix
plt.imshow(corr, cmap='gray')
plt.colorbar()
plt.show()

# Create a correlation matrix
corr = np.corrco