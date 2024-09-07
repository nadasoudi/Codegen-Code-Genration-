def find_tuples(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][0] > lst[j][0]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9