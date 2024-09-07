def length(lst):
    if len(lst) == 0:
        return 0
    else:
        return 1 + length(lst[1:])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(length(lst))

"""

# Python Program to Find the Length of a List Using Iterative Method

def length(lst):
    if len(lst) == 0:
        return 0