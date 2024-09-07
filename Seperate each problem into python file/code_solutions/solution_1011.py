def count_zeros(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
    return count

print(count_zeros([0, 1, 0, 2, 1, 0, 1, 3, 0, 5, 0, 0, 0, 0, 0]))

"""

def count_zeros(nums):