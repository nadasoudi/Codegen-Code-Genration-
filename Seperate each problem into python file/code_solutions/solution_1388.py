# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert a new node at the beginning of the linked list
    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node