def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

# driver code
string = "ABABAC"
sub_string = "ABA"

print(count_substring(string, sub_string))

"""
Output:
6
"""