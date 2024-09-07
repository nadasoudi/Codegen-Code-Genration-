python solution.py

"""

import os
import sys

# Complete the reverse function below.
def reverse(s):
    return s[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverse(s)

    fptr.write(result + '\n')

    fptr.close()