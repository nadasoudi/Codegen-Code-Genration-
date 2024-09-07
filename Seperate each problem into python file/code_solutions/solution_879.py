def arc_length(a, b, c):
    return abs(a - b) + abs(c - b) + abs(a - c) + abs(b - c)

a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))

print("The arc length of", a, "and", b, "is", arc_length(a, b, c))