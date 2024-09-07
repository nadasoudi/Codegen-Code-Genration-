import collections

def solution(arr, k):
    freq = collections.Counter(arr)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return freq[:k]

# Time complexity: O(n)
# Space Complexity: O(n)

# Runtime: 32 ms (96.21%)
# Memory Usage: 14.2 MB (95.74%)

# Runtime: 32 ms (95.74%)
#