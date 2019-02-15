
class Queue:
    def __init__(self):
        self.array = [];
        self.front = 0;
        self.rear = -1;

    def enqueue(self, ele):
        self.array.append(ele)
        self.rear += 1
        return True

    def dequeue(self):
        if self.front > self.rear:
            return
        ele = self.array[self.front]
        self.front += 1
        return ele


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(2)
    queue.enqueue(1)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

