def isSorted(lst):
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return lst[0] == lst[0]
    if lst[0] > lst[1]:
        return False
    return isSorted(lst[1:])

print(isSorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(is