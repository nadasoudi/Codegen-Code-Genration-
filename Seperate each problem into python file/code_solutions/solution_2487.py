def count_leaf_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self