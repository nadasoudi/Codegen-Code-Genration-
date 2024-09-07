def sort_list(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list1[i] = list2[j]
                list2[j] = list1[i]
    return list1, list2

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10