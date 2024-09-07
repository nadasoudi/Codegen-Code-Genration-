def unique_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(unique_list(lst))

"""

# Solution:

def unique_list(lst):
    new_l