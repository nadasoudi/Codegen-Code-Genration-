def solve(self, head):
    if head is None:
        return head
    if head.next is None:
        return head
    slow = head
    fast = head.next
    while fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    slow.next = None
    return slow