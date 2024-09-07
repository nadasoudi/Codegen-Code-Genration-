import collections

def unique_values(d):
    return collections.Counter(d)

print(unique_values({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))

"""