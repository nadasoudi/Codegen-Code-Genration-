import math

def solution(numbers):
    total = 0
    for i in numbers:
        total += math.floor(i/len(numbers))
    return total

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Time complexity: O(n)
# Space Complexity: O(n)

# Runtime: 32 ms (96.41