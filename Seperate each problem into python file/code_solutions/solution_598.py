python solution.py

"""

import os
import sys

def main():
    if len(sys.argv)!= 2:
        print("Usage: python solution.py <file_name>")
        sys.exit(1)
    file_name = sys.argv[1]
    if not os.path.exists(file_name):
        print("File does not exist")
        sys.exit(1)
    with open(file_name