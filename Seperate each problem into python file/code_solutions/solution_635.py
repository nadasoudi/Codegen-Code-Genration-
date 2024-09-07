def smallest_number(nums):
    smallest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
    return smallest

print(smallest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def smallest_number(nums):
    smallest =