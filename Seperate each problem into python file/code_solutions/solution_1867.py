def solution(s):
    rotations = 0
    for i in range(len(s)):
        rotations += s[i]
    return rotations

print(solution("abcdefghijklmnopqrstuvwxyz"))

"""

def solution(s):
    rotations = 0
    for i in range(len(s)):
        rotations += s[i]
    return rotations

print(solution("abcdefghijkl