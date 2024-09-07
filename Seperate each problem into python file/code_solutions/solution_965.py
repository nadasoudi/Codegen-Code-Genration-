def common_elements(l1, l2):
    common_elements = []
    for i in l1:
        for j in l2:
            if i == j:
                common_elements.append(i)
    return common_elements

l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [[1, 2, 3], [4, 5, 6], [7, 8,