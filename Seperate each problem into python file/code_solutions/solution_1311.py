d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

print(list(map(lambda x: dict(x), d.values())))

"""

d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

print(list(map(lambda x: dict(x), d