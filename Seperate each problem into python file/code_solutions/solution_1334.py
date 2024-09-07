def largest_possible_number(nums):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(largest_possible_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def largest_possible_number(nums):
    max_num = 0
    for