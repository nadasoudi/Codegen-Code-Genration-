def count_integer(mixed_list):
    count = 0
    for i in mixed_list:
        if isinstance(i, int):
            count += 1
    return count

print(count_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def count_integer(mixed_list):
    count = 0
    for i in mixed_list:
        if isinstance(i, int):
            count