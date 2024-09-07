def filter_tuples(tup, k):
    return tuple(filter(lambda x: x[k] == tup[k], tup))

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
k = 3
print(filter_tuples(tup, k))

"""

# Solution

def filter_tuples(tup, k):
    return tuple(filter(lambda x: x[k] == tup