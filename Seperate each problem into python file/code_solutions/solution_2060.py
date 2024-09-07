def Queue(size):
    queue = []
    for i in range(size):
        queue.append(i)
    return queue

def printQueue(queue):
    for i in range(len(queue)):
        print(queue[i], end=" ")
    print()

def isEmpty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

def enqueue(queue, item):
    queue.append(item