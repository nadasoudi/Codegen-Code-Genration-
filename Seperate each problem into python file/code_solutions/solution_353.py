def remove_empty_lists(lst):
    for i in range(len(lst)):
        if len(lst[i]) == 0:
            lst.pop(i)
    return lst

lst = [[1, 2, 3], [4, 5, 6], []]
print(remove_empty_lists(lst))

"""

def remove_empty_lists(lst):
    for i in range(len(lst)):