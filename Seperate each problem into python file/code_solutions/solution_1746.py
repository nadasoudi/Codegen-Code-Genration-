def list_to_dict(l):
    d = {}
    for i in l:
        d[i] = l.count(i)
    return d

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_to_dict(l))

"""

# Solution 1

def list_to_dict(l):
    d = {}
    for i in l:
        d[i] = l.count(