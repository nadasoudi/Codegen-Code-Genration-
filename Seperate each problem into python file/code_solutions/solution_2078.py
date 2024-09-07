def LongestSubstringLength(string, k):
    # Write your code here
    if len(string) < k:
        return 0
    if len(string) == k:
        return 1
    if string[0] == string[-1]:
        return LongestSubstringLength(string[1:-1], k)
    else:
        return LongestSubstringLength(string[1:], k) + 1

print(LongestSubstringLength("abcabcbb", 3))
print