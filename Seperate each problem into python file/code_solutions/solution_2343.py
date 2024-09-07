def count_distinct_substrings(string):
    # Write your code here
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                count += 1
    return count

print(count_distinct_substrings("abcdef"))
print(count_distinct_substrings("abcdefghijkl