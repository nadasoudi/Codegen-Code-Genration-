def get_combinations(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        return get_combinations(key + 1, dictionary)

print(get_combinations('a', {'a': 1, 'b': 2, 'c': 3}))

"""

def get_combinations(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else: