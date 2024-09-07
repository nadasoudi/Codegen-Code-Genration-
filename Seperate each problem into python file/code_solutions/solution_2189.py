def count_occurrences(lst, element):
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 5
print(count_occurrences(lst, element))

"""

def count_occurrences(lst, element):
    count = 0
    for i in lst: