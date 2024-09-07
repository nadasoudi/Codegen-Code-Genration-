def check_sequence(patterns, sequence):
    for i in range(len(sequence)):
        if sequence[i] not in patterns:
            return False
    return True

print(check_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def check_sequence(patterns, sequence):
    for i