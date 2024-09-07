def isSubset(lst, sub):
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        return True
    if lst[0] in sub:
        return isSubset(lst[1:], sub)
    else:
        return False

lst = [1, 2, 3, 4, 5]
sub = [4, 5]
print(isSubset(lst, sub