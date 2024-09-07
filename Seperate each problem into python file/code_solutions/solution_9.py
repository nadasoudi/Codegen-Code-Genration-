def insert_after(list, element, n):
    for i in range(n):
        list.insert(i, element)
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5
n = 2
print(insert_after(list, element, n))

"""

def insert_after(list, element, n):
    for i in range(n):
        list