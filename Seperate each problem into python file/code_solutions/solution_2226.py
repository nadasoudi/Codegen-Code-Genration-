import datetime

def convert_python_datetime(dt):
    return dt.replace(tzinfo=datetime.timezone.utc).timestamp()

print(convert_python_datetime(datetime.datetime.now()))

"""

# Solution

import datetime

def convert_python_datetime(dt):
    return dt.replace(tzinfo=datetime.timezone.utc).timestamp()

print(convert_python_datetime(datetime.