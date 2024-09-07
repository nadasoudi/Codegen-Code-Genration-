def max_value(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_value(lst))

"""

# Solution:

def max_value(lst