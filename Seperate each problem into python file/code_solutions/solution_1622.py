def count_lists(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 'L':
                count += 1
    return count

lst = [['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L