def solution(Lambda):
    if Lambda == 0:
        return 1
    else:
        return Lambda + solution(Lambda - 1)

"""

def solution(Lambda):
    if Lambda == 0:
        return 1
    else:
        return Lambda + solution(Lambda - 1)

print(solution(5))