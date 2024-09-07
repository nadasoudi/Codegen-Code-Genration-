def deque(items):
    new_deque = deque()
    for i in items:
        new_deque.append(i)
    return new_deque

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(deque(items))

"""

# Solution 1

def deque(items):
    new_deque = deque()
    for i