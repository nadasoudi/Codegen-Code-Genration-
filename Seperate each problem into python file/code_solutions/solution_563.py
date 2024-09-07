import collections

class Deque(collections.deque):
    def __init__(self, iterable=None):
        super().__init__()
        if iterable is not None:
            self.extend(iterable)

    def append(self, x):
        self.extend(x)

    def extend(self, iterable):
        for i in iterable:
            self.append(i)

    def pop(self):
        return