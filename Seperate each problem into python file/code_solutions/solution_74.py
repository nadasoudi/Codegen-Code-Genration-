def is_greater(list, number):
    for i in range(len(list)):
        if list[i] > number:
            return False
    return True

print(is_greater([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))

"""

def is_greater(list, number):
    for i in range(len(list)):
        if list[i] > number: