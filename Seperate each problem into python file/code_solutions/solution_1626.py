def group_elements(lst, func):
    return len(list(filter(func, lst)))

print(group_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x % 2))

"""

def group_elements(lst, func):
    return len(list(filter(func, lst)))

print(group_elements([1