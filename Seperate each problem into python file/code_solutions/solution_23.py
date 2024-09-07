def solution(numbers):
    return list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

"""

def solution(numbers):
    return list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17