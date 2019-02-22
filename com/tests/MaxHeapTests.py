from unittest import TestCase, main as unittest_main
from com.ds.MaxHeap import MaxHeap


class MaxHeapTests(TestCase):

    def test_insert(self):
        max_heap = MaxHeap()
        max_heap.insert(34)
        self.assertEqual(max_heap.get_max(), 34)

        max_heap.insert(12)
        self.assertEqual(max_heap.get_max(), 34)

        max_heap.insert(56)
        self.assertEqual(max_heap.get_max(), 56)

    def test_extract_max(self):
        max_heap = MaxHeap()
        max_heap.insert(34)
        max_heap.insert(67)
        max_heap.insert(12)
        max_heap.insert(129)
        self.assertEqual(max_heap.extract_max(), 129)
        self.assertNotEqual(max_heap.extract_max(), 12)
        self.assertEqual(max_heap.extract_max(), 34)
        self.assertEqual(max_heap.extract_max(), 12)


if __name__ == '__main__':
    unittest_main()