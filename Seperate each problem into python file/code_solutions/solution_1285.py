def get_index(element, iterable):
    for i, e in enumerate(iterable):
        if e > element:
            return i
    return -1

print(get_index(5, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""

# Solution

def get_index(element, iterable):
    for i, e in enumerate(iterable):