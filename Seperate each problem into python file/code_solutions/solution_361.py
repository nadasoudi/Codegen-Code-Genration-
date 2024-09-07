def check_keys(d, keys):
    for key in keys:
        if key in d:
            print(key, "exists")
        else:
            print(key, "does not exist")

d = {'a': 1, 'b': 2, 'c': 3}
check_keys(d, ['a', 'b', 'c'])

"""

def check_keys(d, keys):
    for key in keys:
        if key in d: