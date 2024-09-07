def remove_keys_with_values_greater_than_k(dict, k):
    for key, value in dict.items():
        if value >= k:
            dict.pop(key)
    return dict

print(remove_keys_with_values_greater_than_k({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 2))

"""

def remove_keys_with_values_great