l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

l3 = []
for i in range(len(l1)):
    for j in range(len(l1[i])):
        l3.append(l1[i][j])

l4 = []
for i in range(len