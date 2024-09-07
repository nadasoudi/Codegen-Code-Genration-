def rotate(lst, n):
    lst.reverse()
    for i in range(n):
        lst.append(lst.pop())
    lst.reverse()
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(rotate(lst, n))

"""

# Solution 1

def rotate(lst, n