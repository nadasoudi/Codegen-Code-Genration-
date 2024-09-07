def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        return [s[0] + permutation(s[1:]) for i in range(len(s))]

print(permutation("abc"))

"""

# Solution 1

def permutation(s):
    if len(s) == 1:
        return [s]
    else:
        return [s[0] + permutation(s[