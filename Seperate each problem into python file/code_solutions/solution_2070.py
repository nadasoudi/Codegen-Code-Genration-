def sort_dict(d):
    return sorted(d.items(), key=itemgetter(1))

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sort_dict(d))

"""

# Solution 1

def sort_dict(d):
    return sorted(d.items(), key=itemgetter(1))

d = {'a': 1, 'b': 2, '