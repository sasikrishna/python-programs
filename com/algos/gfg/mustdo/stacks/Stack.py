'''
Problem statement: Implement stack
'''


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def pop(self):

        if self.top == -1:
            raise Exception('No element to pop.')

        self.top -= 1
        return self.stack.pop()

    def peek(self):
        if self.top == -1:
            raise Exception('No element to peek.')

        return self.stack[self.top]

    def is_empty(self):
        return len(self.stack) == 0

