def common_tuple(list1, list2):
    common_tuple = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                common_tuple.append((list1[i], list2[j]))
    return common_tuple

print(common_tuple([1, 2, 3, 4, 5], [2, 3, 4