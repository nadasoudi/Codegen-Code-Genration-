def break_list(list):
    set_list = []
    for i in list:
        if i not in set_list:
            set_list.append(i)
    return len(set_list) == len(list)

print(break_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(break_list([1, 2, 3, 4, 5, 6,