def count_duplicate(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
    return count

print(count_duplicate([1,2,3,1,2,3]))

"""

def count_duplicate(nums):
    count = 0
    for i in range(len(nums)