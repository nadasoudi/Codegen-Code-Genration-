def split_list(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(split_list(lst))

"""

def split_list(lst):
    return [lst[i:i+3] for i in range(0, len(lst), 3)]

lst