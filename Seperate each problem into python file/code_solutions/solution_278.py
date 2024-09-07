def remove_left(lst):
    return lst[1:]

def remove_right(lst):
    return lst[:-1]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_left(lst))
print(remove_right(lst))

"""

# Solution 1

def remove_left(lst):
    return lst[1:]