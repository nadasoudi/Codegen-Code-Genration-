def create_dict(key_list):
    dict_of_key_value_pairs = {}
    for key in key_list:
        dict_of_key_value_pairs[key] = []
    return dict_of_key_value_pairs

print(create_dict([1, 2, 3, 4, 5]))

"""

# Solution:

def create_dict(key_list):