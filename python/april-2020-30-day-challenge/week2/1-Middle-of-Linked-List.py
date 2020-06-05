from linkedList import ListNode
import unittest


# O(n) time / O(1) space solution
def get_middle_loop(head: ListNode) -> ListNode:
    node = head
    length = 0
    while node:
        length += 1
        node = node.next

    middle = length // 2

    node = head
    for _ in range(middle):
        node = node.next

    return node


# O(n) time/space solution
def get_middle_dict(head: ListNode) -> ListNode:
    node = head
    length = 0
    lookup = {}

    while node:
        lookup[length] = node
        length += 1
        node = node.next

    return lookup[length // 2]


# O(n) time / two pointer solution
def get_middle(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


class TestMiddle(unittest.TestCase):
    def test_12345(self):
        head = ListNode.build([1, 2, 3, 4, 5])
        self.assertEqual(get_middle(head), head.next.next)

    def test_123456(self):
        head = ListNode.build([1, 2, 3, 4, 5, 6])
        self.assertEqual(get_middle(head), head.next.next.next)


if __name__ == "__main__":
    unittest.main()
