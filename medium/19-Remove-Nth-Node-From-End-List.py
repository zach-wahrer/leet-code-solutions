from models.linkedList import ListNode
import unittest


def remove_nth_node_from_end(head: ListNode, n: int) -> ListNode:
    pass


class TestRemovedNode(unittest.TestCase):
    def test_12345_2(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2, 3, 4, 5]), 2)
        output = ListNode.build([1, 2, 3, 5])
        self.assertEqual(input, output)

    def test_12_1(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2]), 1)
        output = ListNode.build([1])
        self.assertEqual(input, output)

    def test_1_1(self):
        input = remove_nth_node_from_end(ListNode.build([1]), 1)
        output = ListNode.build([])
        self.assertEqual(input, output)

    def test_123_2(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2, 3]), 2)
        output = ListNode.build([1, 3])
        self.assertEqual(input, output)

    def test_123456789_8(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8)
        output = ListNode.build([1, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(input, output)

    def test_123456789_9(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        output = ListNode.build([2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
