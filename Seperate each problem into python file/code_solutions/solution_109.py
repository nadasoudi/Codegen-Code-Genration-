def max_min(numbers):
    if len(numbers) == 0:
        return None
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    if len(numbers) == 3:
        return numbers[0], numbers[1], numbers[2]
    if len(numbers) == 4:
        return numbers[0