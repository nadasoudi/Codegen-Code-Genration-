def move_zeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = '0'
    return nums

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(move_zeros(nums))

"""

# Solution:

def move_zeros(nums):
    for i