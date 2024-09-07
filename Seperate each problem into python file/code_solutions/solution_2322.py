def solution(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vowels:
            print(i, end="")

solution("aAaEeIiOoUu")

"""

def solution(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vowels: