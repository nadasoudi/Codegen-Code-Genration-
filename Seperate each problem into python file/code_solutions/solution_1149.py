def atLeastN(list, n):
    for i in range(len(list)):
        if list[i] < n:
            return False
    return True

print(atLeastN([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

"""

def atLeastN(list, n):
    for i in range(len(list)):
        if list[i] < n: