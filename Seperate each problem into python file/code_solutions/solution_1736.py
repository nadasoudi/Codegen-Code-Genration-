def convert_dict_to_list(dictionary):
    list_of_lists = []
    for key, value in dictionary.items():
        list_of_lists.append([key, value])
    return list_of_lists

dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h