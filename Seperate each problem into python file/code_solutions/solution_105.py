def permutations(nums):
    if len(nums) == 1:
        return 1
    else:
        return sum(permutations(nums[1:]))

print(permutations([1, 2, 3]))

"""

# Solution 1

def permutations(nums):
    if len(nums) == 1:
        return 1
    else:
        return sum(permutations(nums[1:]))

print(perm