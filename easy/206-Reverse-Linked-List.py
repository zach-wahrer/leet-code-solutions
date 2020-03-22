import unittest
from models.linkedList import ListNode


def reverse_ll(head: ListNode):
    pass


class TestReverseList(unittest.TestCase):

    def test_12345(self):
        head = ListNode.build([1, 2, 3, 4, 5])
        reversed = ListNode.build([5, 4, 3, 2, 1])
        self.assertEqual(reverse_ll(head), reversed)

    def test_1(self):
        head = ListNode.build([1])
        reversed = ListNode.build([1])
        self.assertEqual(reverse_ll(head), reversed)

    def test_blank(self):
        head = ListNode.build([])
        reversed = ListNode.build([])
        self.assertEqual(reverse_ll(head), reversed)
