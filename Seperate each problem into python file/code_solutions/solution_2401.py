def sort_dict(d):
    return sorted(d.items(), key=lambda item: item[1])

d = {'a': 1, 'b': 2, 'c': 3}
print(sort_dict(d))

"""

# Solution

def sort_dict(d):
    return sorted(d.items(), key=lambda item: item[1])

d = {'a': 1, 'b': 2, 'c': 3}