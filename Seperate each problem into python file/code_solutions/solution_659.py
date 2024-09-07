def removeKth(lst, k):
    return lst[:k] + lst[k+1:]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
print(removeKth(lst, k))

"""

def removeKth(lst, k):
    return lst[:k] + lst[k+1:]

lst =