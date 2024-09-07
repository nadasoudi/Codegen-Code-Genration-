def max_count(d):
    max_count = 0
    for key in d:
        count = d[key]
        if count > max_count:
            max_count = count
    return max_count

d = {'a': 1, 'b': 2, 'c': 3}
print(max_count(d))

"""

def max_count(d):
    max_count = 0
    for key in d:
        count = d[key]
        if