def deep_copy(d):
    new_d = {}
    for key in d:
        new_d[key] = d[key]
    return new_d

d = {'a': 1, 'b': 2, 'c': 3}
print(deep_copy(d))

"""

# Solution

def deep_copy(d):
    new_d = {}
    for key in d:
        new_d[key] = d[