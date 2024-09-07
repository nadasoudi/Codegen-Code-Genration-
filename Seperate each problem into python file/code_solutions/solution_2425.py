def search(head, element):
    if head is None:
        return False
    if head.data == element:
        return True
    if head.data > element:
        return search(head.next, element)
    return search(head.next, element)

# Driver Code
if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.