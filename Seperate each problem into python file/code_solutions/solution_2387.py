def solution(a, k):
    answer = []
    for i in a:
        if i[0] % k == 0:
            answer.append(i)
    return answer

print(solution([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)], 3))

"""

def solution(a, k):
    answer = []
    for i in a:
        if i