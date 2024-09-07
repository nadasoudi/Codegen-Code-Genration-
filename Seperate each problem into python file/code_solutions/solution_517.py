def last_element(lst):
    for i in range(len(lst)):
        if lst[i] == last_element(lst[i:]):
            return i
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(last_element(lst))

"""

def last_element(lst):
    for i in range