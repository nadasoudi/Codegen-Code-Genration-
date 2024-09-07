def solution(words):
    # Write your code here
    word_set = set(words)
    word_set = sorted(word_set)
    return len(word_set)

print(solution(["cba","bab","bac"]))
print(solution(["a","a","b","b","b"]))
print(solution(["a","a","b","b","b","b"]))
print(solution(["a","a","b","b