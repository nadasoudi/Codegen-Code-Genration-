def binary_search(list, target):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

print(binary_search([1,