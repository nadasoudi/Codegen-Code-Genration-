def get_combinations(digits):
    combinations = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i + j == digits:
                combinations.append(str(i) + str(j))
    return combinations

print(get_combinations('123'))

"""

# Solution 1

def get_combinations(digits):
    combinations = []