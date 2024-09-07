def even_odd(numbers):
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_odd(numbers))

"""

# Solution 1

def even_odd(numbers):