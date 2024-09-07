def multiply(d):
    for i in d:
        d[i] = d[i] * 10
    return d

d = {'a': 1, 'b': 2, 'c': 3}
print(multiply(d))

"""

# Solution:

def multiply(d):
    for i in d:
        d[i] = d[i] * 10
    return d

d = {'a': 1, 'b': 2, 'c