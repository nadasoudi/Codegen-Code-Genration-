import numpy as np

# Convert degrees to centigrade
degrees = np.deg2rad(np.arange(0, 360, 10))

# Convert degrees to fahrenheit
fahrenheit = np.deg2rad(degrees)

# Convert degrees to centigrade
centigrade = np.rad2deg(fahrenheit)

# Print the values
print(centigrade)