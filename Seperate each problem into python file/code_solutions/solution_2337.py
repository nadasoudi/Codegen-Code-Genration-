def max_record_value(d):
    max_value = 0
    for key in d:
        if d[key] > max_value:
            max_value = d[key]
    return max_value

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(max_record_value(d))

"""

"""

def max_record_value(d):
    max_value = 0
    for key in d