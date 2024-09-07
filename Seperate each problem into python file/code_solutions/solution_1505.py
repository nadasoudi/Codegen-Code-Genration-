def solution(names):
    return sum([len(name.split('.')[0].lower()) for name in names])

"""

def solution(names):
    return sum([len(name.split('.')[0].lower()) for name in names])

print(solution(["Alex", "Brian", "Chris", "Dave", "Eve", "Fred", "George", "George", "George",