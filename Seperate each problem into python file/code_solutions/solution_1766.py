def solution(files):
    answer = []
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
        answer.append(content)
    return answer

print(solution(["a.txt", "b.txt", "c.txt"]))

"""

def solution(files):
    answer = []
    for file in files:
        with open(file, 'r') as f:
            content = f.read()