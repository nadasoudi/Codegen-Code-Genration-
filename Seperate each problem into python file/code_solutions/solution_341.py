def delete_node(node):
    node.next.prev = node.prev
    node.prev.next = node.next
    node.prev = None
    node.next = None

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# This code is contributed