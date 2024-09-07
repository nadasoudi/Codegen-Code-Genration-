import numpy as np

# Read the image
img = np.array(Image.open('image.jpg'))

# Convert the image to NumPy array
img_np = np.array(img)

# Save the NumPy array as a CSV file
np.savetxt('image.csv', img_np, delimiter=',')

# Open the CSV file as a Python code
with open('image.csv', 'r') as f:
    # Read the CSV file