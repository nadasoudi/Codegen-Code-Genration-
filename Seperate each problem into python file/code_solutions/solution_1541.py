import arrow

def time_difference(time1, time2):
    time1 = arrow.get(time1)
    time2 = arrow.get(time2)
    diff = time1 - time2
    return diff.humanize()

print(time_difference("2021-05-01", "2021-05-02"))

"""

# Solution:

from datetime import datetime

def time_difference(