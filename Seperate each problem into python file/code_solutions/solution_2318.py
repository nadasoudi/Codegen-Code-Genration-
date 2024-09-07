import numpy as np
import csv

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a csv file
with open('my_file.csv', 'w') as f:
    # Create the csv writer
    csv_writer = csv.writer(f)
    # Write the data
    csv_writer.writerows(arr)

# Open the file in