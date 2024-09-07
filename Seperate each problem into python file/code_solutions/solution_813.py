def split_list(lst):
    first_part = lst[:len(lst)//2]
    second_part = lst[len(lst)//2:]
    return first_part, second_part

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(split_list(lst))

"""

def split_list(lst):