def solution(A):
    return [A[i] for i in range(len(A)) if A[i] % 2 == 0]

"""

def solution(A):
    return [A[i] for i in range(len(A)) if A[i] % 2 == 0]

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8