def max_values(d):
    max_values = {}
    for key, value in d.items():
        if value not in max_values:
            max_values[value] = key
        else:
            max_values[value] = key
    return max_values

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(max_values(d))

"""

"""