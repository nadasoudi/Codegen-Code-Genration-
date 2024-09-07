def reverse(head, n):
    if head is None:
        return None
    if n == 1:
        return head
    return reverse(head.next, n-1)

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # insert at the beginning