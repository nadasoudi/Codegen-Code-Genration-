# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to delete the last item from a singly linked list
    def deleteLast(self):
        if self.head is None:
            return None
        
        # If the list is empty, return