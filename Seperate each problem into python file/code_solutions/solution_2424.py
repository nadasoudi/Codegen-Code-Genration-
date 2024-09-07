def solution(n):
    for i in range(1, n+1):
        if i % 5 == 0 and i % 7 == 0:
            print(i, end=" ")

if __name__ == '__main__':
    n = int(input())
    solution(n)