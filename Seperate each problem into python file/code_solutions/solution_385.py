import collections

class Solution:
    def __init__(self):
        self.d = collections.defaultdict(list)
    
    def add(self, key, value):
        self.d[key].append(value)
    
    def get(self, key):
        return self.d[key][0]
    
    def remove(self, key):
        self.d[key].pop(0)
    
    def get_unique(self):