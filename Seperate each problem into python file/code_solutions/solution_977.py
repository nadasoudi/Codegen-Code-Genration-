def diff(nums):
    return nums[nums[0]] - nums[nums[nums[0] + 1]]

n = int(input())
nums = [int(x) for x in input().split()]
print(diff(nums))

# Solution:

# def diff(nums):
#     return nums[nums[0]] - nums[nums[nums