def product(lst):
    return reduce(lambda x, y: x * y, lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(product(lst))

"""

# Solution:

def product(lst):
    return reduce(lambda x, y: x * y, lst)

lst = [1, 2, 3, 4, 5, 6, 7,