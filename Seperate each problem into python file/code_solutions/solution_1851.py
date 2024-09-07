def intersection(l1, l2):
    l1.sort()
    l2.sort()
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            return l1[i], l2[j]
    return l1[i], l2[