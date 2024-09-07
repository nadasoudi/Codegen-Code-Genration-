def convert_list_to_tuple(lst):
    tuple_list = []
    for i in lst:
        tuple_list.append(tuple(i))
    return tuple_list

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(convert_list_to_tuple(lst))

"""

# Solution 1

def convert_list_to_tuple(lst