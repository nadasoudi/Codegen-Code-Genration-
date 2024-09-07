def solution(words, n):
    answer = []
    for word in words:
        if len(word) > n:
            answer.append(word)
    return answer

print(solution(["i", "love", "leetcode", "i", "love", "coding"], 2))

# Time complexity: O(n)
# Space Complexity: O(n)

# Runtime: 32 ms (96.41%)
#