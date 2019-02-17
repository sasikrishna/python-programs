from unittest import TestCase, main as unittest_main
from com.ds.SingleLinkedList import SingleLinkedList


class SingleLinkedListsTest(TestCase):

    def test_add(self):
        list = SingleLinkedList();
        list.add(5)
        list.add(9)
        list.add(145)
        self.assertTrue(list.contains(5))
        self.assertTrue(list.contains(9))
        self.assertFalse(list.contains(133))

    def test_remove(self):
        list = SingleLinkedList()
        list.add(5)
        list.add(9)
        list.add(145)
        self.assertTrue(list.remove(5))
        self.assertTrue(list.remove(145))
        self.assertFalse(list.remove(1))


if __name__ == '__main__':
    unittest_main()
