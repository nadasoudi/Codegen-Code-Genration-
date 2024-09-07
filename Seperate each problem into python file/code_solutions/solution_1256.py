def shallow_copy(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
    return new_lst

lst = [1, 2, 3, 4, 5]
print(shallow_copy(lst))

"""

# Solution 1

def shallow_copy(lst):
    new_lst = []
    for i in lst:
        new_lst.