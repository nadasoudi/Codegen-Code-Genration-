def last_occurrence(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 5
print(last_occurrence(lst, item))

"""

def last_occurrence(lst, item):
    for i in range