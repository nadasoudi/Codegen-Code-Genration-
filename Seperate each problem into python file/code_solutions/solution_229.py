def pair_up(lst):
    for i in range(len(lst)):
        if i == 0:
            lst[i], lst[i+1] = lst[i+1], lst[i]
        else:
            lst[i], lst[i-1] = lst[i-1], lst[i]
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8