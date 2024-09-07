def unique_values(d):
    for key in d:
        if d[key] == 1:
            print(key)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
unique_values(d)

"""

def unique_values(d):
    for key in d:
        if d[key] == 1:
            print(key)

d = {'a': 1, 'b