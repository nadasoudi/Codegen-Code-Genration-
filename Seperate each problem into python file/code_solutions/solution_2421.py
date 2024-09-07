def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n):
    if n == 0:
        return 0
    elif