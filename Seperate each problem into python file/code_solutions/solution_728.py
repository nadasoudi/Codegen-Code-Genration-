def invert_dict(d):
    d = dict(d)
    for key in d:
        d[key] = key
    return d

d = {'a': 1, 'b': 2, 'c': 3}
print(invert_dict(d))

"""

# Solution:

def invert_dict(d):
    d = dict(d)
    for key in d:
        d[key] = key
    return