def is_unique(lst):
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(is_unique(lst))

"""

# Solution 1

def is_unique(lst):
    return len(set(lst)) == len(lst)