def sort_by_index(lst, index):
    return sorted(lst, key=lambda x: x[index])

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sort_by_index(lst, 0))

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sort_by_index(lst