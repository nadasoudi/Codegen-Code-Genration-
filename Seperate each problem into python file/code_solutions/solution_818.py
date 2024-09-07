def solution(numbers):
    answer = []
    for i in numbers:
        if int(i, 2) % 5 == 0:
            answer.append(i)
    return answer

print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,