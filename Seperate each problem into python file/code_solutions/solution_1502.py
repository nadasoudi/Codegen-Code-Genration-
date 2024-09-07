def check_all(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True

print(check_all([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

"""

def check_all(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True