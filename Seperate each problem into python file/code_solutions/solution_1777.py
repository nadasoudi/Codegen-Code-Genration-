def solution(head):
    # Write your code here
    if head is None:
        return None
    
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    slow.next = None
    
    return slow

# This is the class of the input linked list.
# class ListNode:
#     def __init__(self, x):
#