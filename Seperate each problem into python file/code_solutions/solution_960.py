import datetime

# create a datetime object
dt = datetime.datetime(2021, 8, 1, 12, 30, 0, 0)

# print the datetime object
print(dt)

# create a datetime object with the same hour, minute, second, microsecond and timezone info
dt = datetime.datetime(2021, 8, 1, 12, 30, 0, 0, tzinfo=datetime.