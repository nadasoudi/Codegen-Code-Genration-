def remove_item(lst, item):
    for i in range(len(lst)):
        if lst[i][0] == item:
            lst.pop(i)
    return lst

lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(remove_item(lst, 5))

"""

def remove_