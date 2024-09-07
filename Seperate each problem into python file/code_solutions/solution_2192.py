def flatten(lst):
    return ''.join(lst)

print(flatten([1, 2, 3, 4, 5]))

"""

# Solution 1

def flatten(lst):
    return ''.join(lst)

print(flatten([1, 2, 3, 4, 5]))

# Solution 2

def flatten(lst):
    return ''.join(lst[0]) + ''.join(lst[1])