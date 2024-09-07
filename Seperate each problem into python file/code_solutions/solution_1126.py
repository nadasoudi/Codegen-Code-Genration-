def sum_of_numbers(nums):
    sum = 0
    for num in nums:
        if num < 0:
            sum += num
    return sum

print(sum_of_numbers([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))

"""

def sum_of_numbers(nums):
    sum = 0
    for num