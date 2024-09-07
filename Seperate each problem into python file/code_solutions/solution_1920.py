import sys

def stack_solver(stack, stack_switcher):
    while stack:
        print(stack.pop())
    print(stack_switcher)

if __name__ == '__main__':
    stack_solver(stack, stack_switcher)

"""

# Solution

import sys

def stack_solver(stack, stack_switcher):
    while stack:
        print(stack.pop())
    print(stack_switcher)