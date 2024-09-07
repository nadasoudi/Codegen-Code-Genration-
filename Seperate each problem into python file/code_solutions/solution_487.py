def solution(lst, x):
    for i in range(len(lst)):
        if lst[i] > x:
            return i
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 10
print(solution(lst, x))

"""

def solution(lst, x):
    for i in range(len(lst