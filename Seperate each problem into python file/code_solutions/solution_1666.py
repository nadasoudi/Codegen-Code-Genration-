def add_two_lists(list1, list2):
    for i in range(len(list1)):
        list1[i] += list2[i]
    return list1

print(add_two_lists([1, 2, 3], [4, 5, 6]))

"""

def add_two_lists(list1, list2):
    for i in range(len(list1)):
        list1[