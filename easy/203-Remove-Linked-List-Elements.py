import unittest
from models.linkedList import ListNode


def remove_linked_list_val(head: ListNode) -> ListNode:
    pass


class TestRemovedLinkedList(unittest.TestCase):
    def test_1263456_6(self):
        input = remove_linked_list_val(ListNode.build([1, 2, 6, 3, 4, 5, 6]), 6)
        self.assertEqual(input, ListNode.build(1, 2, 3, 4, 5))

    def test_1578092_0(self):
        input = remove_linked_list_val(ListNode.build([-1, 5, 7, 0, 9, 2]), 0)
        self.assertEqual(input, ListNode.build(-1, 5, 7, 9, 2))

    def test_9_9(self):
        input = remove_linked_list_val(ListNode.build([9]), 9)
        self.assertEqual(input, ListNode.build(None))

    def test_9_1(self):
        input = remove_linked_list_val(ListNode.build([9]), 1)
        self.assertEqual(input, ListNode.build(9))

    def test_blank(self):
        input = remove_linked_list_val(ListNode.build([]), None)
        self.assertEqual(input, ListNode.build(None))

    def test_12_1(self):
        input = remove_linked_list_val(ListNode.build([1, 2]), 1)
        self.assertEqual(input, ListNode.build(2))

    def test_12_2(self):
        input = remove_linked_list_val(ListNode.build([1, 2]), 2)
        self.assertEqual(input, ListNode.build(1))


if __name__ == "__main__":
    unittest.main()
