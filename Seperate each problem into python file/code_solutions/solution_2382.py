def group_similar(d, v):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

d = {'a': 1, 'b': 2, 'c': 3}
v = ['a', 'b', 'c']
print(group_similar(d, v))

"""

# Solution:

def group_similar(d, v):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)