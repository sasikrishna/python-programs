class Stack:
    """"
    Stack implementation in python.
    """

    def __init__(self):
        self.stack = [];
        self.top = -1;

    def push(self, value):
        self.stack.append(value);
        self.top += 1;
        return True;

    def peek(self):
        if self.top == -1:
            return;

        return self.stack[self.top];

    def pop(self):
        if self.top == -1:
            return;
        ele = self.stack[self.top];
        self.stack.pop(self.top);
        self.top -= 1;
        return ele;

    def print_stack(self):
        print(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.print_stack()
    print('Element at top is ', stack.pop());
    stack.print_stack()
    print('Element at top is ', stack.pop());
    stack.print_stack()
    stack.push(1)
    stack.print_stack()
    print('Element at top is ', stack.pop());
    print('Element at top is ', stack.pop());
    print('Element at top is ', '- OOPS Stack is empty' if stack.peek() == None else stack.pop());
