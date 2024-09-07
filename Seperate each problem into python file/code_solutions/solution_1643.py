def split_every_nth(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(split_every_nth(lst, n))

"""

def split_every_nth(lst, n):
    return [lst[i:i+