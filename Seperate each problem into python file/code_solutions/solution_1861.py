def get_unique_combination(l1, l2):
    l1.sort()
    l2.sort()
    result = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                result.append([l1[i], l2[j]])
    return result

l1 = [1, 2, 3, 4, 5]
l2 = [1