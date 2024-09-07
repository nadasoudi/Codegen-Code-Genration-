def reverse_list(head):
    if head is None:
        return None
    
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Code to test the above function
# head = [1, 2, 3, 4, 5]
# head = reverse_list(head)
# print(head.val)

# Solution 2