def highest_3_values(d):
    for key in d:
        if d[key] > 3:
            print(key, d[key])

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
highest_3_values(d)

"""

def highest_3_values(d):
    for key in d:
        if d[key] > 3:
            print(key, d[key