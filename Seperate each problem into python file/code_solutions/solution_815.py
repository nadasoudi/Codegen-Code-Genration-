def iter_range(start, stop, step):
    while start < stop:
        yield start
        start += step

print(list(iter_range(1, 10, 2)))

"""

def iter_range(start, stop, step):
    while start < stop:
        yield start
        start += step

print(list(iter_range(1, 10, 2)))

"""

def iter_range(start,