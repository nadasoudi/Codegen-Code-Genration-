def count_elements(list, start, end):
    count = 0
    for i in list:
        if i >= start and i <= end:
            count += 1
    return count

print(count_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9))

"""

def count_elements(list, start, end):
    count = 0
    for i in list:
        if