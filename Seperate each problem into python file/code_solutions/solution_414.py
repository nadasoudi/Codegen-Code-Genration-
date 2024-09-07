def solution(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                count += 1
    return count

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(lst))

"""

def solution