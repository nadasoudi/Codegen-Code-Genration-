def nested_dict_to_dict(lst):
    d = {}
    for i in lst:
        d[i] = nested_dict_to_dict(i)
    return d

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nested_dict_to_dict(lst))

"""

def nested_dict_to_dict(lst):
    d = {}
    for