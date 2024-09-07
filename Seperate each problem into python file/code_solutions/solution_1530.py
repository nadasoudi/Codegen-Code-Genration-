def remove_strings(lst):
    for i in lst:
        lst.remove(i)
    return lst

lst = [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
print(remove_strings(lst))

"""

def remove_strings(lst):
    for i in lst:
        lst.remove(i)
    return lst