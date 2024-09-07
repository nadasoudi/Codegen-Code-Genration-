def lcm(x, y):
    if x > y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            lcm = i
    return lcm

print(lcm(12, 24))

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lcm