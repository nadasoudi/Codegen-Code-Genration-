def divide(lst1, lst2):
    return [x / y for x, y in zip(lst1, lst2)]

lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8, 10]

print(divide(lst1, lst2))

"""

# Solution:

def divide(lst1, lst2):
    return [x / y for x