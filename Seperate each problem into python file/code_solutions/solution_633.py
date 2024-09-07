def shortest_distance(s, c):
    # Write your code here
    return [i for i in range(len(s)) if s[i] == c]

print(shortest_distance('abcdefghijklmnopqrstuvwxyz', 'z'))

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8