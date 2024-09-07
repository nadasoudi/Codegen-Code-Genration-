def solution(str):
    lst = list(map(int, str))
    lst.sort()
    return lst

print(solution("abcd"))

# Time complexity: O(n)
# Space Complexity: O(n)

# Solution 2:

def solution(str):
    lst = list(map(int,