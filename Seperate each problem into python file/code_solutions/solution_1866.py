def LRU(cache, capacity):
    if cache.get(capacity) is not None:
        return cache[capacity]
    else:
        return None

cache = OrderedDict()
cache[1] = 1
cache[2] = 2
cache[3] = 3
cache[4] = 4
cache[5] = 5
cache[6] = 6
cache[7] = 7
cache[8] = 8
cache[9] = 9
cache[10] = 10
cache[