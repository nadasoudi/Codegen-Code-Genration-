import datetime

# Convert the datetime object to a string
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Convert the string to a datetime object
print(datetime.datetime.strptime('2021-10-10 12:12:12', '%Y-%m-%d %H:%M:%S'))

# Convert the