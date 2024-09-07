def extract_first(lst, index):
    if index == 0:
        return lst[0]
    else:
        return lst[index]

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(extract_first(lst, 0))
print(extract_first(lst, 1))
print(extract_first(lst, 2))
print(extract_