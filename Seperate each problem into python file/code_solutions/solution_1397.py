def check_lists(list1, list2):
    if len(list1)!= len(list2):
        return False
    for i in range(len(list1)):
        if list1[i]!= list2[i]:
            return False
    return True

print(check_lists([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(check_lists([1, 2, 3, 4,