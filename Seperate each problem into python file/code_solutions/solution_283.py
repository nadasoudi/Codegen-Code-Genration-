def count_doubly_linked_list(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

# Test your solution
head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_doubly_linked_list(head))

# Output:
# 5
# 6
# 7
# 8
# 9
# 10