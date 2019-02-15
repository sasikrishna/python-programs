from com.ds.Queue import Queue
from unittest import TestCase


class QueueTests(TestCase):
    def test_queue(self):
        queue = Queue()
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), None)
        self.assertTrue(queue.enqueue(45))
        queue.enqueue(89)
        self.assertNotEqual(queue.dequeue(), 89)


if __name__ == '__main__':
    QueueTests.main()
