import os

def largestFile(directory):
    # Open the file for reading
    f = open(directory, 'r')
    # Read the file line by line
    for line in f:
        # If the line is not empty
        if line:
            # Split the line into words
            words = line.split()
            # If the word is the first word
            if words[0] == 'File':
                # Open the file for writing
                w = open(words[1], 'w')