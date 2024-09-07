def rotate(d, n):
    for i in range(n):
        d.append(d.popleft())
    return d

# Driver Code
d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(rotate(d, 3))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)