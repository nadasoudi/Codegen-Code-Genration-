def sort_nested_keys(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            sort_nested_keys(value)
        else:
            dictionary[key] = value
    return dictionary

dictionary = {'a': 1, 'b': 2, 'c': 3}
print(sort_nested_keys(dictionary))

"""

"""

"""

"""

"""

"""

"""