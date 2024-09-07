def smallest(numbers):
    smallest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest

print(smallest(numbers))

"""

# Solution 1

def smallest(numbers):
    smallest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest