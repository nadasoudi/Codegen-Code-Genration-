def xor_linked_list(head, k):
    if head is None:
        return None
    if head.next is None:
        return head
    if head.next.next is None:
        return head
    if head.next.next.next is None:
        return head
    if head.next.next.next.next is None:
        return head
    if head.next.next.next.next.next is None:
        return head
    if head.next.next.next