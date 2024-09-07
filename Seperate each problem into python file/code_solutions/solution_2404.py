def sum_dict(d):
    sum = 0
    for key in d:
        sum += d[key]
    return sum

d = {'a': 1, 'b': 2, 'c': 3}
print(sum_dict(d))

"""

# Solution 1

def sum_dict(d):
    sum = 0
    for key in d:
        sum += d[key]
    return sum

d = {'a': 1, 'b':