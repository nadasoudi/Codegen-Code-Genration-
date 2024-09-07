import collections

class Deque:
    def __init__(self):
        self.items = collections.deque()

    def isEmpty(self):
        return self.items == collections.deque()

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def