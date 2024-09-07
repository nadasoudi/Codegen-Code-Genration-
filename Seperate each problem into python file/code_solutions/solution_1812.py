import collections

def remove_tuples(lst):
    # create a new list with all None values removed
    new_lst = []
    for i in lst:
        if i is not None:
            new_lst.append(i)
    return new_lst

lst = [1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, 10]
print(remove_tuples(lst))

# Solution