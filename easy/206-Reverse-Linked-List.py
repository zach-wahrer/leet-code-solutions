import unittest
from models.linkedList import ListNode


# O(n) space/time solution
def reverse_ll_iterative(head: ListNode):
    ll_vals = []
    node = head
    while node:
        ll_vals.append(node.val)
        node = node.next
    ll_vals.reverse()
    node = head
    for i in ll_vals:
        node.val = i
        node = node.next

    return head


# Recursive O(n) time/space solution
def reverse_ll(head: ListNode):
    if not head:
        return []

    ll_vals = []

    def _get_vals(node, ll_vals):
        if node.next:
            _get_vals(node.next, ll_vals)
        ll_vals.append(node.val)

    def _put_vals(node, ll_vals):
        if node.next:
            _put_vals(node.next, ll_vals)
        node.val = ll_vals.pop()

    _get_vals(head, ll_vals)
    _put_vals(head, ll_vals)
    return head


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


if __name__ == "__main__":
    unittest.main()
