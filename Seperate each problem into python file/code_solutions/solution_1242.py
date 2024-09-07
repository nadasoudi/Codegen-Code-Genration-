def combine_lists(list1, list2):
    d = {}
    for i in list1:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in list2:
        if i not in d:
            d[i] = 1