from models.linkedList import ListNode
import unittest


# Slow/Fast Solution, O(n) time, O(1) space
# Set fast to n positions ahead of slow
# Iterate through linked list till fast.next hits None
# Remove slow
# Edge Cases: Removing First Element, 1 element lists
def remove_nth_node_from_end(head: ListNode, n: int) -> ListNode:
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next

    if not fast:  # n = first item edge case
        head = slow.next
        if not head:  # list of one item edge case
            head = ListNode("")
        return head

    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


class TestRemovedNode(unittest.TestCase):

    def test_12345_2(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2, 3, 4, 5]), 2)
        output = ListNode.build([1, 2, 3, 5])
        self.assertEqual(input, output)

    def test_12_1(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2]), 1)
        output = ListNode.build([1])
        self.assertEqual(input, output)

    def test_12_2(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2]), 2)
        output = ListNode.build([2])
        self.assertEqual(input, output)

    def test_1_1(self):  # Test works on LeetCode, but not here
        input = remove_nth_node_from_end(ListNode.build([1]), 1)
        output = ListNode.build("")
        self.assertEqual(input, output)

    def test_123_3(self):
        input = remove_nth_node_from_end(ListNode.build([1, 2, 3]), 3)
        output = ListNode.build([2, 3])
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
