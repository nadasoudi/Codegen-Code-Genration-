def get_value(d, selector):
    for key in d:
        if selector in d[key]:
            return d[key][selector]

print(get_value({'a': {'b': {'c': 'd'}}, 'c': 'd'}, 'b'))

"""

def get_value(d, selector):
    for key in d:
        if selector in d[key]:
            return