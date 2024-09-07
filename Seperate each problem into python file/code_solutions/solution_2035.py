def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

# Enter your code here. Read input from STDIN. Print output to STDOUT
string, sub_string = input(), input()
count = count_substring(string, sub_string)
print(count)

'''

# Enter