def reverse_row(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j][0] > lst[j + 1][0]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]