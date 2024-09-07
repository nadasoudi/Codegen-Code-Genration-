import numpy as np

def f(x):
    return np.sin(x)

x = np.linspace(0, 2*np.pi, 100)
y = f(x)

# Plot the function
plt.plot(x, y)

# Create a new figure
plt.figure()

# Create a new axes
ax = plt.axes()

# Plot the function
ax.plot(x, y)

# Create a new figure
plt.figure