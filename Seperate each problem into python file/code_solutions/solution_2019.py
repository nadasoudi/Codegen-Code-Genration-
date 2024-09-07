def search(head, x):
    if head is None:
        return False
    if head.data == x:
        return True
    if head.data > x:
        return search(head.next, x)
    return search(head.next, x)

# Driver Code
if __name__ == '__main__':
    head = CircularLinkedList()
    head.append(1)
    head.append(2)
    head.append(3)