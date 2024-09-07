def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    else:
        return root
    return root

def delete(root, key):
    if root is None:
        return None
    if key < root.data:
        root