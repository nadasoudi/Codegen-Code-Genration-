def solution(strs):
    count = 0
    for i in range(len(strs)):
        if len(strs[i]) >= 2 and strs[i][0] == strs[i][-1]:
            count += 1
    return count

print(solution(["aba", "cdc", "aaab", "ccb"]))
print(solution(["a",