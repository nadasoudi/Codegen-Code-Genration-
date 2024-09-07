def interleave(l1, l2, l3):
    return [l1[i] + l2[i] + l3[i] for i in range(len(l1))]

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = [11, 12, 13, 14, 15]

print(interleave(l1, l2, l3))

"""

def