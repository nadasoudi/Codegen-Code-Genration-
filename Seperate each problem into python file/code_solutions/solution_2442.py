def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

print(count_digits(123))

"""

# Solution 1

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

print(count_digits(123))

# Solution 2

def count_digits(