def min_value(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min_value(lst))

"""

def min_value(lst):
    min_