def compare_lists(list1, list2):
    if len(list1)!= len(list2):
        return False
    for i in range(len(list1)):
        if list1[i]!= list2[i]:
            return False
    return True

print(compare_lists([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(compare_lists([