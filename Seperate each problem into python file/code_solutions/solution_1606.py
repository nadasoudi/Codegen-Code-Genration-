def gnome_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

lst = [10, 5, 2, 3, 1, 7, 4, 6, 8, 9]
print(gnome_sort