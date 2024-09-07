def second_smallest(numbers):
    smallest = numbers[0]
    for i in range(1, len(numbers)):
        if smallest > numbers[i]:
            smallest = numbers[i]
    return smallest

print(second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def second_smallest(numbers):
    smallest = numbers[0]
    for i in