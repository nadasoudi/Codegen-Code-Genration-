import os
import sys
import csv

# Open the file in read mode
with open('data.csv', 'r') as csvfile:
    # Split the data into a list of individual lines
    lines = csv.reader(csvfile)
    # Read the header row first (skip this step if there is now header)
    next(lines)
    # Iterate over each row in the csv
    for row in lines:
        # Print each row
        print