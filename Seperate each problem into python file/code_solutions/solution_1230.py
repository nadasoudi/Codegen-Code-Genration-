def longest_common_substring(str1, str2):
    # Write your code here
    if len(str1) > len(str2):
        return str1
    else:
        return str2

print(longest_common_substring("abcde", "abcde"))
print(longest_common_substring("abcde", "abcdea"))
print(longest_common_substring("abcde", "abcdea", 2))
print