def deque(n):
    deque = collections.deque()
    for i in range(n):
        deque.append(i)
    return deque

n = int(input("Enter the number of elements to be added to the left and right sides: "))
print("The elements are: ", end="")
for i in range(n):
    print(deque(i+