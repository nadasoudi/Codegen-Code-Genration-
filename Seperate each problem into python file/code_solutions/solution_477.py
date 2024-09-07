def set_item(item, index):
    new_item = item
    new_index = index
    new_node = Node(new_item)
    new_node.next = head
    head = new_node
    index = new_index
    return head, index

# Code to test the above function
item = 'item'
index = 0
head, index = set_item(item, index)
print(head.data, index)