def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

# driver code
string = "abracadabra"
sub_string = "ab"
print(count_substring(string, sub_string))

# This code is contributed by Nikhil