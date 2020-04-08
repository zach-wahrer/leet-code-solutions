from linkedList import ListNode
import unittest


def get_middle(head: ListNode) -> ListNode:
    pass


class TestMiddle(unittest.TestCase):
    def test_12345(self):
        head = ListNode().build([1, 2, 3, 4, 5])
        self.assertEqual(get_middle(head), head.next.next)

    def test_123456(self):
        head = ListNode().build([1, 2, 3, 4, 5, 6])
        self.assertEqual(get_middle(head), head.next.next.next)
