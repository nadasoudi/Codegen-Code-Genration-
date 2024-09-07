def remove_elements(lst, ele):
    return [i for i in lst if i!= ele]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ele = 7

print(remove_elements(lst, ele))

"""

# Solution:

def remove_elements(lst, ele):
    return [i for i in lst if i!= ele]