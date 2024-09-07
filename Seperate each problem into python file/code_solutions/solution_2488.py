# Open the file for reading
f = open("mbox-short.txt")

# Read the file line by line
for line in f:
    # If the line is not empty
    if line:
        # Split the line into words
        words = line.split()
        # Count the number of words
        print(len(words))

# Close the file
f.close()

"""

# Open the file for reading
f = open("mbox-short.txt")

#