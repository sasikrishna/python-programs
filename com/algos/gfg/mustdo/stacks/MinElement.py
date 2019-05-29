'''
Problem statement: You are given N elements and your task is to Implement a Stack in which you can get minimum element
in O(1) time.
'''

from com.algos.gfg.mustdo.stacks.Stack import Stack

if __name__ == '__main__':
    test_cases = int(input())

    queries_count, operations_list = [], []
    for i in range(test_cases):
        queries_count.append(int(input()))
        operations_list.append(list(map(int, input().split())))

    for i in range(test_cases):
        stack, minStack = Stack(), Stack()
        operations = operations_list[i]

        j = 0
        while j < len(operations):

            # Operation 1 means pushing to stack.
            if operations[j] == 1:
                j += 1
                stack.push(operations[j])

                # Updating min stack
                if minStack.is_empty() or operations[j] < minStack.peek():
                    minStack.push(operations[j])

            # Operation 2 means poping element from stack
            elif operations[j] == 2:

                if not stack.is_empty() and not minStack.is_empty() and stack.peek() == minStack.peek():
                    minStack.pop();

                print(stack.pop() if not stack.is_empty() else -1, end=" ")

            # Operation 3 means peeking min element
            else:
                print(minStack.peek() if not minStack.is_empty() else -1, end=" ")

            j += 1

        print()

