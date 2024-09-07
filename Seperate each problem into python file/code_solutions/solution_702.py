def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))

"""

def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(isPalindrome("A man,