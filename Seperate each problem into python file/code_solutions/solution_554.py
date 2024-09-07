def sum_of_positive_ints(n):
    sum = 0
    for i in range(1, n+1):
        if i > 0:
            sum += i
    return sum

print(sum_of_positive_ints(10))

"""

# Solution

def sum_of_positive_ints(n):
    sum = 0
    for i in range(1, n