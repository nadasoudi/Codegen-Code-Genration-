import os

def check_access(path):
    if os.access(path, os.R_OK):
        print("Access granted")
    else:
        print("Access denied")

check_access("C:\\Users\\srin\\Desktop\\Python\\Python_Projects\\Python_Projects_2\\test.txt")

"""

#!/bin/python3

import math
import os