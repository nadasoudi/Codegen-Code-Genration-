def remove_none(lst):
    for i in range(len(lst)):
        if lst[i] is None:
            lst.pop(i)
    return lst

lst = [1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10]
print(remove_none(lst))

"""

# Solution:

def remove_none(lst):
    for i in range(len(l