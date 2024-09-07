def diff(list1, list2):
    diff = []
    for i in range(len(list1)):
        diff.append(list1[i] - list2[i])
    return diff

print(diff([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))

"""

def diff(list1, list2):
    diff = []
    for i in range(len(list1)):
        diff.append(list1[i]