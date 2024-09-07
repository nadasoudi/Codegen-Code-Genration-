# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.val, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = ListNode(data)
            return