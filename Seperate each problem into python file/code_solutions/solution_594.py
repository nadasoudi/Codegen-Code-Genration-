def insert_after(list, n, element):
    for i in range(n):
        list.insert(i, element)
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
element = 5
insert_after(list, n, element)
print(list)

"""

def insert_after(list, n, element):
    for i in range(n):