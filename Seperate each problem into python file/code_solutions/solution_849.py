def flatten(lst):
    if len(lst) == 0:
        return []
    else:
        return flatten(lst[0]) + flatten(lst[1:])

lst = [1, 2, [3, 4, [5, [6, 7]], 8]]
print(flatten(lst))

"""

def flatten(lst):
    if len(lst) == 0:
        return []
    else: