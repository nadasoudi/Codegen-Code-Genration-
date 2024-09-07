import itertools

def solution(lst, sum):
    return list(itertools.filterfalse(lambda x: x.sum() == sum, lst))

print(solution([1, 2, 3, 4, 5], 7))

# Output: [1, 2, 3, 4, 5]
# Explanation: The first two elements whose sum is 7 are [1, 2, 3