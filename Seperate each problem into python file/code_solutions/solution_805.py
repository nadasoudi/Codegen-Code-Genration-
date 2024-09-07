def sum_of_groups(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i]!= 0:
            sum += nums[i]
    return sum

print(sum_of_groups([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def sum_of_groups(nums):