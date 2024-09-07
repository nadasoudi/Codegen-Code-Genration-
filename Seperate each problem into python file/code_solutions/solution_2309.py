def isPalindrome(s):
    # Write your code here
    stack = []
    for i in s:
        if i.isalnum():
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] == i:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(isPalind