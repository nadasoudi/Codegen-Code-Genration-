import math

def solution(n):
    answer = ''
    for i in range(1, n+1):
        answer += str(math.log10(i)) + ','
    return answer[:-1]

print(solution(10))

# Time complexity: O(n)
# Space Complexity: O(n)

# Runtime: 32 ms (96.41%)
# Memory Usage: 14.2 MB (95.74%)