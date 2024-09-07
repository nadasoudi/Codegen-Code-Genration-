def nth_evil_number(n):
    if n == 1:
        return 1
    else:
        return nth_evil_number(n-1) + nth_evil_number(n-2)

n = int(input("Enter the number: "))
print(nth_evil_number(n))

"""

# Solution

def nth_evil_number(n):
    if n == 1:
        return 1
    else:
        return nth_evil_number(