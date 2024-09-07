def create_key_value_list(dictionary):
    key_value_list = []
    for key, value in dictionary.items():
        key_value_list.append((key, value))
    return key_value_list

dictionary = {'a': 1, 'b': 2, 'c': 3}
print(create_key_value_list(dictionary))

"""

# Solution:

def create_key_value_list(d