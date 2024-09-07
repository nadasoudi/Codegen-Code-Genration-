def permutations(string, n):
    if n == 0:
        print(string)
    else:
        for i in range(len(string)):
            permutations(string[:i] + string[i + 1:], n - 1)

permutations("abcd", 3)

"""

def permutations(string, n):
    if n == 0:
        print(string)
    else:
        for i in range(len