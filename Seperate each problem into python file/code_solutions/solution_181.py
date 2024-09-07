def merge_list(list1, list2):
    list1.extend(list2)
    return list1

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(merge_list(list1, list2))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Output: [1, 2, 3,