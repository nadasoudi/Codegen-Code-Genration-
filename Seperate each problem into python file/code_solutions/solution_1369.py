import collections

class Deque:
    def __init__(self):
        self.items = collections.deque()

    def add_front(self, item):
        self.items.appendleft(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.popleft()