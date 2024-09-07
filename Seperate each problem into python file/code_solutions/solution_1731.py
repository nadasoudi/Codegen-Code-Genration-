def solution(priorities, location):
    heap = []
    for i in range(len(priorities)):
        heapq.heappush(heap, priorities[i])
    
    for i in range(location, len(priorities)):
        if heapq.heappop(heap) > heapq.heappop(priorities):
            return i
    return -1

# Test
print(solution([1, 1, 9,