import datetime

def convert_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

dt = datetime.datetime(2021, 1, 1, 12, 30, 0)
print(convert_datetime(dt))

"""

# Solution 1

import datetime

def convert_datetime(dt):
    return dt.strftime('%Y-%m-%d