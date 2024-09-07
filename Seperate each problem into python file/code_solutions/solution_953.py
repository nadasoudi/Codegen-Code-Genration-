def nested_dict_to_dict(nested_list):
    dictionary = {}
    for i in range(len(nested_list)):
        dictionary[i] = nested_list[i]
    return dictionary

nested_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nested_dict_to_dict(nested_list))

"""

# Solution

def nested_dict_to