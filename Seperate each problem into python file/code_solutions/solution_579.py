def move_end(lst, n):
    lst.append(lst[-n])
    del lst[-n:]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
move_end(lst, n)
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3