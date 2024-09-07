#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getPerimeter function below.
def getPerimeter(a, b, c):
    return (a + b + c) * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arad = input