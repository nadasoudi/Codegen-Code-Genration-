import arrow

# create a datetime object
dt = arrow.now()

# create a string representation of the datetime object
print(dt.format('YYYY-MM-DD HH:mm:ss'))

# create a datetime object from a string representation
dt = arrow.get(dt.format('YYYY-MM-DD HH:mm:ss'))

# create a string representation of the datetime object
print(dt.format('