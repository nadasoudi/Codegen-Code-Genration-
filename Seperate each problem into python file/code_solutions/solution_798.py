def drop_empty(d):
    for i in d:
        if d[i] == []:
            del d[i]
    return d

d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
print(drop_empty(d))

"""

def drop_empty(d):
    for i in d:
        if d[i] == []:
            del d[i