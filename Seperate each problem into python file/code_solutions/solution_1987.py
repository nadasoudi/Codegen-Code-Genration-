def sum_digits(n):
    return sum(int(i) for i in str(n))

n = int(input("Enter a number: "))
print(sum_digits(n))

"""

# Solution 1

def sum_digits(n):
    return sum(int(i) for i in str(n))

n = int(input("Enter a number: "))
print(sum_digits(n))

# Solution 2

def sum_dig