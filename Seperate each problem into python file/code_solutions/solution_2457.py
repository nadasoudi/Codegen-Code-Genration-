def solution(arr):
    max_even = 0
    max_odd = 0
    for i in arr:
        if i % 2 == 0:
            max_even += i
        else:
            max_odd += i
    if max_even > max_odd:
        return max_even
    else:
        return max_odd

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(