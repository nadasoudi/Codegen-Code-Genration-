def group(lst, fn):
    return list(map(fn, lst))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fn = lambda x: x**2
print(group(lst, fn))

"""

# Solution 1

def group(lst, fn):
    return list(map(fn, lst))

lst = [1, 2, 3, 4,