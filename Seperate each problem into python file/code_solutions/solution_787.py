def max_min(lst):
    max = lst[0]
    min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_min(lst))

"""

# Solution 1