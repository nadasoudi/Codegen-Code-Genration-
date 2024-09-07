def remove_key(d, key):
    if key in d:
        del d[key]
    else:
        print("Key not found")

d = {'a': 1, 'b': 2, 'c': 3}
remove_key(d, 'a')
print(d)

"""

def remove_key(d, key):
    if key in d:
        del d[key]
    else:
        print("Key not found")

d = {'