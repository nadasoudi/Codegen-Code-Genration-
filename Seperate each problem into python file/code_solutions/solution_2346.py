def convert_list_to_list_of_lists(list_of_dictionaries):
    list_of_lists = []
    for dictionary in list_of_dictionaries:
        list_of_lists.append([dictionary['name'], dictionary['age'], dictionary['gender'], dictionary['height'], dictionary['weight']])
    return list_of_lists

print(convert_list_to_list_of_lists([{'name': 'John', '