def is_palindrome(s):
    if len(s) == 1:
        return True
    if s[0] == s[-1]:
        return True
    else:
        return False

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))

"""

# Solution 1

def is_palindrome(s):
    if len(s) == 1: