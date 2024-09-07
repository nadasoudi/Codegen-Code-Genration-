def permutations(string):
    if len(string) == 1:
        return [string]
    else:
        return [string[0] + permutations(string[1:]) for i in range(len(string))]

print(permutations('abcd'))

"""

def permutations(string):
    if len(string) == 1:
        return [string]
    else:
        return [string[0] + permutations(string[