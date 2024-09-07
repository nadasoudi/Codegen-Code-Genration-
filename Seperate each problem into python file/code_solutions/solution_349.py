def combine_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        result[key] = dict1[key]
    for key in dict2:
        result[key] = dict2[key]
    return result

print(combine_dicts({"a": 1, "b": 2}, {"c": 3, "d": 4, "e": 5}))

"""

"""

"""