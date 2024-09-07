def uncommon_elements(l1, l2):
    l1.sort()
    l2.sort()
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            i += 1
            j += 1
        else:
            i += 1
    return l1[i:], l2[j:]

l1 = [1, 2, 3, 4, 5,