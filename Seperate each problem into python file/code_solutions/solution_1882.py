def invert_dict(d):
    for k, v in d.items():
        d[v] = k
    return d

d = {'a': 1, 'b': 2, 'c': 3}
print(invert_dict(d))

"""

# Solution:

def invert_dict(d):
    for k, v in d.items():
        d[v] = k
    return d

d = {'a': 1, 'b': 2, '