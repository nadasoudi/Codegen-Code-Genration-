def solution(a, b):
    answer = []
    for i in range(len(a)):
        for j in range(len(b)):
            answer.append(a[i] * b[j])
    return answer

print(solution([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))

"""

def solution(a, b):
    answer = []