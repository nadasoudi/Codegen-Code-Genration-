def pairs(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            yield lst[i], lst[j]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(pairs(lst)))

"""

def pairs(lst):
    for i in range(len(l