def duplicate_finder(list):
    duplicate_list = []
    for i in list:
        if list.count(i) > 1:
            duplicate_list.append(i)
    return duplicate_list

print(duplicate_finder([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,