def remove_duplicates(d):
    new_dict = {}
    for key, value in d.items():
        if value not in new_dict:
            new_dict[value] = key
    return new_dict

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(remove_duplicates(d))

"""

"""

"""

"""

"""

"""

"""