def group_sublists(lst):
    d = {}
    for i in range(len(lst)):
        if lst[i] not in d:
            d[lst[i]] = []
        d[lst[i]].append(i)
    return d

lst = [1,2,3,4,5,6,7,8,9,10]
print(group_sublists(lst))

"""

def group_sublists(l