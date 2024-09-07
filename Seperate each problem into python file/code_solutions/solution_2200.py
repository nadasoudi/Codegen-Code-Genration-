def nested_dict_to_tuple(nested_dict):
    # create a tuple from the nested dictionary
    return tuple(nested_dict.items())

# create a dictionary from the nested dictionary
nested_dict = {
    'a': {
        'b': {
            'c': 1
        }
    }
}

# convert the nested dictionary to a tuple
print(nested_dict_to_tuple(nested_dict))

# create a dictionary