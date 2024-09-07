def common_items(list1, list2):
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

print(common_items([1, 2, 3, 4, 5], [2, 3, 5, 6, 7]))

"""

def common_items(list1, list2):
    common_items = []
    for item in list1:
        if item