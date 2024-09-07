def get_largest_and_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    return largest, smallest

print(get_largest_and_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# OUTPUT:
#