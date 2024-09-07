def count_times(deque, element):
    count = 0
    for i in deque:
        if i == element:
            count += 1
    return count

# driver code
deque = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
element = 'a'
print(count_times(deque, element))

# Output:
# 3
# 3
#