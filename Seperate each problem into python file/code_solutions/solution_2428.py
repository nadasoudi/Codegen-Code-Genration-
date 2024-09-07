def sqrt(x):
    if x == 0:
        return 0
    else:
        return x**0.5

print(sqrt(4))

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the'solve' function below.
def solve(a, b):
    if b == 0:
        return a
    else:
        return solve(a, b//2) + 1

if __name__ ==