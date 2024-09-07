def count_pair(list1, list2):
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1
    return count

print(count_pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def count_pair(