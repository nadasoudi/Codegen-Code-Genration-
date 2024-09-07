#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split()
    s = list(map(int, s))
    s.sort()
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], '