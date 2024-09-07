import datetime

def datetime_to_arrow(dt):
    return dt.replace(tzinfo=datetime.timezone.utc).astimezone(datetime.timezone.utc)

dt = datetime.datetime(2021, 1, 1, 12, 30, 0, tzinfo=datetime.timezone.utc)
print(datetime_to_arrow(dt))

"""

# Solution: