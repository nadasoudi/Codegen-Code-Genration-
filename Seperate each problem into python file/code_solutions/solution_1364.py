def remove_sublist(lst, start, end):
    for i in range(start, end):
        lst.remove(lst[i])
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_sublist(lst, 0, 9))

"""

def remove_sublist(lst, start, end):
    for