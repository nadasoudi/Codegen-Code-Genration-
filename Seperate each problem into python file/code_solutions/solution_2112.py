def convert_list_to_dict(list):
    dict = {}
    for i in range(len(list)):
        dict[list[i][0]] = list[i][1]
    return dict

print(convert_list_to_dict([('a', 1), ('b', 2), ('c', 3)]))

"""

def convert_list_to_dict(list):
    dict = {}
    for i in range(len(list)):
        dict[