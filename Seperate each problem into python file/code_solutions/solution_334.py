def interleave(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
print(interleave(l1, l2))

"""

def interleave(l1, l2):
    return [l1[i] + l2[i] for i in