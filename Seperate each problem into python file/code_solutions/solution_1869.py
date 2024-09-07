def change_dict(d):
    for key, value in d.items():
        d[key] = value + 1
    return d

d = {'a': 1, 'b': 2, 'c': 3}
print(change_dict(d))

"""

# Solution

def change_dict(d):
    for key, value in d.items():
        d[key] = value + 1
    return d

d = {'a': 1, 'b': 2, '