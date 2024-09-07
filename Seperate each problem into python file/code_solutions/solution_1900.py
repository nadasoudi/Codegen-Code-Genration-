def sort_tuple(tup):
    return tup[0]

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sorted(tup, key=sort_tuple))

"""

# Solution 1

def sort_tuple(tup):
    return tup[0]

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sorted