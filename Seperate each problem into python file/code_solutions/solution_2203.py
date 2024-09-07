def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += sum(map(int, str(i)))
    return answer

"""

def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += sum(map(int, str(i)))
    return answer

"""

def solution(n):
    answer = 0
    for i in range(1, n