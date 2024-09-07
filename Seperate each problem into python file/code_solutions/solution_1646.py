def max_occurrences(lst, item):
    max_occurrences = 0
    for i in lst:
        if i == item:
            max_occurrences += 1
    return max_occurrences

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 9
print(max_occurrences(lst, item))

"""

def max_occurrences(lst