def min_max(lst):
    min_val = lst[0][0]
    max_val = lst[0][0]
    for i in range(1, len(lst)):
        if lst[i][0] < min_val:
            min_val = lst[i][0]
        if lst[i][0] > max_val:
            max_val = lst[i][0