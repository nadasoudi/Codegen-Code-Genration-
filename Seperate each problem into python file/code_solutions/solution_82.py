def count_substring(string, k):
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                count += 1
    return count

print(count_substring("ABAB", 2))

"""

def count_