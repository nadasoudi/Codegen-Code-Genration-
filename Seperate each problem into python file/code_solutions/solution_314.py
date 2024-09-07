def rotate(d, n):
    for i in range(n):
        d.append(d.popleft())
    return d

# Driver Code
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.append(7)
d.append(8)
d.append(9)
d.