def add_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] + 1
    return numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_numbers(numbers))

"""

# Solution 1

def add_numbers(numbers):
    for i in range(len(numbers)):