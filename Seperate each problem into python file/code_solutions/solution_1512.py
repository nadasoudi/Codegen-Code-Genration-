def convert_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            d[key] = convert_dict(value)
        elif isinstance(value, list):
            d[key] = [convert_dict(i) for i in value]
    return d

d = {'a': 1, 'b': 2, 'c': 3}
print(convert_dict(d))