def combinations(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]

lst = [1, 2, 3, 4, 5]
n = 4
print(combinations(lst, n))

"""

# Solution:

def combinations(lst, n):
    return [lst[i:i+n] for i in range(len(