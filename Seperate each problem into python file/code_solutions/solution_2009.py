def solution(k, words):
    answer = []
    for word in words:
        if len(word) > k:
            answer.append(word)
    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

"""

def solution(k, words):
    answer = []
    for word in words:
        if len(word) > k:
            answer.