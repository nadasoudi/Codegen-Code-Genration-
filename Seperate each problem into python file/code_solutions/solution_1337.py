def get_diff(list1, list2):
    diff = []
    for i in range(len(list1)):
        diff.append(list1[i] - list2[i])
    return diff

print(get_diff([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

"""

def get_diff(list1, list2):
    diff = []
    for i in range(len(list1)):