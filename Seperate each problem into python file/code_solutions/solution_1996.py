def max_consecutive_substring(string):
    max_consecutive_substring = 0
    for i in range(len(string)):
        if string[i] == string[i+1]:
            max_consecutive_substring += 1
        else:
            max_consecutive_substring = max(max_consecutive_substring, i+2)
    return max_consecutive_substring

print(max_consecutive_substring