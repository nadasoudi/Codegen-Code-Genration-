def sort_mixed_list(mixed_list):
    mixed_list.sort(key=lambda x: x[0])
    mixed_list.sort(key=lambda x: x[1])
    mixed_list.sort(key=lambda x: x[2])
    mixed_list.sort(key=lambda x: x[3])
    return mixed_list

print(sort_mixed_list([[