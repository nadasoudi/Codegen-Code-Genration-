import collections

def count_words(filename):
    """
    Count the frequency of words in a file.
    """
    # Open the file for reading
    infile = open(filename, 'r')
    # Read the file line by line
    for line in infile:
        # Split the line into words
        words = line.split()
        # Count the number of words
        count = len(words)
        # Print the number of words
        print(count, words)