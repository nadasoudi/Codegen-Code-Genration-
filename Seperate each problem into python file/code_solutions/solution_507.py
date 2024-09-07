python solution.py input.txt

"""

import sys

def main():
    try:
        file_name = sys.argv[1]
        file = open(file_name, 'r')
        count = 0
        for line in file:
            count += len(line.split())
        print(count)
    except IndexError:
        print("File name missing")
    except FileNotFoundError:
        print("File