def swap_two_sublists(list1, list2):
    list1[0], list1[1] = list1[1], list1[0]
    list2[0], list2[1] = list2[1], list2[0]
    return list1, list2

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(swap_two_sublists(list1