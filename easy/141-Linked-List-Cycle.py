from models.linkedList import ListNode
import unittest


def has_cycle(head: ListNode) -> bool:
    pass


class TestLinkedListCycle(unittest.TestCase):
    def test_3204_true(self):
        input = has_cycle(ListNode.build_circular([3, 2, 0, -4]))
        self.assertTrue(input)

    def test_12_true(self):
        input = has_cycle(ListNode.build_circular([1, 2]))
        self.assertTrue(input)

    def test_1_false(self):
        input = has_cycle(ListNode.build([1]))
        self.assertFalse(input)

    def test_blank_false(self):
        input = has_cycle(ListNode.build([]))
        self.assertFalse(input)

    def test_12345678_false(self):
        input = has_cycle(ListNode.build([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertFalse(input)


if __name__ == "__main__":
    unittest.main()
