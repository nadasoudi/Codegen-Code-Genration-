def solution(lst):
    for i in range(len(lst)):
        if lst[i] == lst[0]:
            return i
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(lst))

# Output:
# 5
# Explanation:
# The first element is at index 0.
# The second