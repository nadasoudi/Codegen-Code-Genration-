python solution.py first.txt second.txt

"""

import sys

def read_file(filename):
    """Read the file and return a list of lines"""
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except IOError:
        print ("Error: Can't find the file", filename)
        sys.exit()

def write_file(filename, lines):
    """Write the file with