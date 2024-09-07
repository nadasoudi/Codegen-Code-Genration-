def search(head, item):
    if head is None:
        return False
    if head.data == item:
        return True
    return search(head.next, item)

# Test
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next