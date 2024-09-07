def group_similar(lst):
    lst_copy = lst.copy()
    lst_copy.sort()
    for i in range(len(lst_copy)):
        for j in range(i+1, len(lst_copy)):
            if lst_copy[i] == lst_copy[j]:
                lst_copy[i], lst_copy[j] = lst_copy[j], lst_copy[i]