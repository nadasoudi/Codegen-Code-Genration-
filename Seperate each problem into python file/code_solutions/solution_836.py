import random

def interleave(lst1, lst2):
    return list(map(list, zip(*lst1, *lst2)))

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

print(interleave(lst1, lst2))

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8,