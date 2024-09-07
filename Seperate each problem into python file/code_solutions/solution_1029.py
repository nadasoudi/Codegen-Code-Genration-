def solution(lst, func):
    for i in range(len(lst)):
        if func(lst[i]):
            print(i)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = lambda x: x % 2 == 0

solution(lst, func)

"""

def solution(lst, func):
    for i in range(