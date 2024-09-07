def diff(list1, list2):
    diff = []
    for i in range(len(list1)):
        if list1[i]!= list2[i]:
            diff.append(list1[i])
    return diff

print(diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def diff(