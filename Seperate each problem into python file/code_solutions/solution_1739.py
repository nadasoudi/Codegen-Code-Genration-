import time

def unix_to_date(unix_time):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(unix_time))

print(unix_to_date(1568692800))

"""

# Solution 1

import time

def unix_to_date(unix_time):
    return time.strftime("%Y-%m-%d %H: