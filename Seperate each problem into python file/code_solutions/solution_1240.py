def common_member(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print(common_member([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))

"""

def common_member(list1, list2):
    for i in list1:
        for j in list2:
            if