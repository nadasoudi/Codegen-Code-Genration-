def remove_empty_list(lst):
    for i in range(len(lst)):
        if lst[i] == []:
            lst.pop(i)
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_empty_list(lst))

"""

# Solution

def remove_empty_list(lst):
    for i in range(len(lst)):