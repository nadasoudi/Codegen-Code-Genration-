def count_tuple(lst):
    count = 0
    for i in lst:
        if isinstance(i, tuple):
            count += 1
    return count

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_tuple(lst))

"""

# Solution:

def count_tuple(lst):
    count = 0
    for i in lst