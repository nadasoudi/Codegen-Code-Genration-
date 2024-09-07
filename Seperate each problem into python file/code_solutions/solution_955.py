l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l.sort(key=lambda x: x[0])

print(l)

l.sort(key=lambda x: x[1])

print(l)

l.sort(key=lambda x: x[2])

print(l)

l.sort(key=lambda x: x[0])

print(l)