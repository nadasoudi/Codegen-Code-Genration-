def check_priority(op1, op2, op3, op4):
    if op1 + op2 + op3 + op4 == 10:
        return True
    else:
        return False

print(check_priority(1, 2, 3, 4))
print(check_priority(1, 2, 3, -4))
print(check_priority(1, 2, 3, 5))
print(check_priority(1, 2, 3, -