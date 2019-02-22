from unittest import TestCase
from unittest import main as unittest_main
from com.ds.DoubleLinkedList import DoubleLinkedList


class DoubleLinkedListTests(TestCase):

    def test_insert_begining(self):
        list = DoubleLinkedList()
        list.insert_begining(34)
        self.assertTrue(list.head.data, 34)

        list.insert_begining(42)
        self.assertTrue(list.head.data, 42)

        list.insert_begining(39)
        self.assertTrue(list.head.data, 39)

    def test_insert_end(self):
        list = DoubleLinkedList()
        list.insert_end(34)
        self.assertTrue(list.head.data, 34)

        list.insert_end(42)
        self.assertTrue(list.head.data, 34)

    def remove(self):
        list = DoubleLinkedList()
        list.insert_end(34)
        list.insert_end(68)
        list.insert_begining(32)
        list.insert_begining(78)

        self.assertTrue(list.remove(78))
        self.assertTrue(list.remove(32))
        self.assertFalse(list.remove(23))
        self.assertTrue(list.remove(34))
        self.assertTrue(list.remove(68))


if __name__ == '__main__':
    unittest_main()
