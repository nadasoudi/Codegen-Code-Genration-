def solution(low, high):
    for i in range(low, high+1):
        if i < 0:
            continue
        if i % 2 == 0:
            print(i, end=" ")
        else:
            print(i, end=" ")
            print(i, end=" ")
            print(i, end=" ")
            print(i, end=" ")
            print(i, end=" ")
            print(i, end=" ")
            print(