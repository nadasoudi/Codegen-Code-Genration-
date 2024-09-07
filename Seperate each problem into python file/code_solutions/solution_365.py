def solution(str_list):
    # your code goes here
    return [[str_list[i:i+3]] for i in range(0, len(str_list), 3)]

print(solution(["a", "b", "c", "d", "e", "f"]))

"""

def solution(str_list):
    # your code goes here
    return [[str_list[i:i+3]] for i in range(0, len(