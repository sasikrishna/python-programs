from com.ds.Stack import Stack
from unittest import TestCase, main as unittest_main


class StackTest(TestCase):

    def test_stack_push(self):
        stack = Stack();
        self.assertEqual(stack.peek(), None);
        stack.push(5);
        self.assertEqual(stack.peek(), 5);
        stack.push(4);
        self.assertEqual(stack.peek(), 4);
        stack.push(3);
        self.assertEqual(stack.peek(), 3);

    def test_stack_pop(self):
        stack = Stack();
        stack.push(5);
        stack.push(4);
        stack.push(3);
        self.assertEqual(stack.pop(), 3);
        self.assertEqual(stack.pop(), 4);
        self.assertEqual(stack.pop(), 5);
        self.assertEqual(stack.pop(), None);


if __name__ == '__main__':
    unittest_main();
