def solution(record, K, x):
    answer = []
    for i in record:
        if i.count(K) > 0:
            answer.append(i)
    return answer

# Test
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"],3,4))

# Output
# Enter uid1234 Muzi
# Enter u