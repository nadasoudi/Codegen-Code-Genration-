import heapq

def merge_sorted_lists(l1, l2):
    heapq.heapify(l1)
    heapq.heapify(l2)
    res = []
    while l1 and l2:
        if l1[0] < l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))
    while l1:
        res