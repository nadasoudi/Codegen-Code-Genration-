#!/usr/bin/env python

import json

def main():
    # Open the file
    inFile = open('text.txt', 'r')
    # Read the file line by line
    for line in inFile:
        # Convert each line to a dictionary
        line = line.strip()
        d = json.loads(line)
        # Print the dictionary
        print(d)
    # Close the file
    inFile.close()

if __name__ == '__main__':