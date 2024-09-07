def filter_list(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter_list(lst))

"""

# Solution

def filter_list(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

lst = [1, 2, 3, 4