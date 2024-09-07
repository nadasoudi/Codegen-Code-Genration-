def middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head = [1, 2, 3, 4, 5]

print(middle(head))

# Output:
# 5
# 2
# 3
# 4
# 5

# Explanation:
# The middle element is 2.
# The middle element is the middle element.
#