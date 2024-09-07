def odd_items(lst):
    odd_items = []
    for i in lst:
        if i % 2!= 0:
            odd_items.append(i)
    return odd_items

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(odd_items(lst))

"""

# Solution:

def odd_items(lst):
    odd_items = []
    for i in