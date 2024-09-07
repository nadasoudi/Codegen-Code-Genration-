def common_index(lst1, lst2):
    common_index = []
    for i in range(len(lst1)):
        if lst1[i] in lst2:
            common_index.append(lst1[i])
    return common_index

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [1, 2, 3, 4, 5,