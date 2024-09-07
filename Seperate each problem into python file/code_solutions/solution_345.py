def sum_dict(d):
    sum = 0
    for i in d.values():
        sum += i
    return sum

d = {'a': 1, 'b': 2, 'c': 3}
print(sum_dict(d))

"""

# Solution

def sum_dict(d):
    sum = 0
    for i in d.values():
        sum += i
    return sum

d = {'a': 1, 'b': 2, '