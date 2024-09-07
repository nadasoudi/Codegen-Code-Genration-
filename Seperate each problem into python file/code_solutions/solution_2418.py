import random

def generate_random_binary_string(length):
    binary_string = ''
    for i in range(length):
        binary_string += str(random.randint(0,1))
    return binary_string

print(generate_random_binary_string(5))

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Write your code here