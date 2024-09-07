def solution(n):
    if n == 1:
        return 1
    else:
        return solution(n-1) + solution(n-2)

print(solution(5))

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20