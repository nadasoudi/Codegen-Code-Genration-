def solution(arr):
    # Write your code here
    count = 0
    for i in arr:
        if i > 0:
            count += 1
        elif i < 0:
            count -= 1
        else:
            count = 0
    return count

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(arr))

arr = [1, 2