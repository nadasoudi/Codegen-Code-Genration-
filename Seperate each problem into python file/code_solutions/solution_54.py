def diff(nums):
    diff = 0
    for i in range(1, len(nums)):
        diff += nums[i] - nums[i-1]
    return diff

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(diff(nums))

"""

def diff(nums):
    diff = 0
    for i in range(1, len(nums)