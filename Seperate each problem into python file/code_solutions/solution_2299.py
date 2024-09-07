def sort_by_column(lst, column):
    return sorted(lst, key=lambda x: x[column])

lst = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(sort_by_column(lst, 0))

"""

# Solution

def sort_by_column(lst, column):
    return sorted(lst, key=lambda x: x[column])

lst = [('