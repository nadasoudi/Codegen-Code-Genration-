import arrow

def get_dst(time):
    return arrow.get(time).timezone.dst(arrow.get(time).time)

print(get_dst('2021-05-01'))

"""

# Solution

import arrow

def get_dst(time):
    return arrow.get(time).timezone.dst(arrow.get(time).time)

print(get_dst('2021-05-01'