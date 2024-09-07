def sum_amicable_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
        else:
            if i % 3 == 0:
                sum += i
    return sum

print(sum_amicable_numbers(100))

"""

def sum_amicable_numbers(n):
    sum = 0
    for i in range(1, n +