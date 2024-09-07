def contains_sublist(lst, sublist):
    for i in range(len(lst)):
        if lst[i] in sublist:
            return True
    return False

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contains_sublist(lst, sublist))