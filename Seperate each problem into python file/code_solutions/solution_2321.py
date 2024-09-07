def remove_tuples(k):
    return tuple(tuple(t) for t in list(enumerate(range(k))))

print(remove_tuples(3))

"""

# Solution

def remove_tuples(k):
    return tuple(tuple(t) for t in list(enumerate(range(k))))

print(remove_tuples(3))