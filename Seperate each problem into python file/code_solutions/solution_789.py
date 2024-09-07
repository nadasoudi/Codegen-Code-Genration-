def common_elements(l1, l2):
    l1 = list(set(l1))
    l2 = list(set(l2))
    common = []
    for i in l1:
        for j in l2:
            if i == j:
                common.append(i)
    return common

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 2, 3