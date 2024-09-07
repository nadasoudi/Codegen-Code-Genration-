def max_min(nums):
    max_num = nums[0]
    min_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
        if nums[i] < min_num:
            min_num = nums[i]
    return max_num, min_num