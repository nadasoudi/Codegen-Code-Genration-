def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    else:
        return [nums[0] + [nums[i] for i in range(len(nums)) if i!= nums[i]] for nums in permute(nums[1:])]

print(permute([1, 2, 3]))

"""