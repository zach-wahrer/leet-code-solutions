'''
Psudocode:
    Iterate through linked list
        Check if we've seen value before
        If not add it
    Build output linked list
    Return it

'''

import unittest
from models.linkedList import ListNode


def remove_dupes(head: ListNode) -> ListNode:
    if head:
        node = ListNode(head.val)
        head = head.next
    else:
        return ListNode("")
    new_head = node
    while head:
        if head.val != node.val:
            node.next = ListNode(head.val)
            node = node.next
        head = head.next
    return new_head


class TestForRemovedDupes(unittest.TestCase):

    def test_112(self):
        input = remove_dupes(ListNode.build([1, 1, 2]))
        output = ListNode.build([1, 2])
        self.assertEqual(input, output)

    def test_11112233(self):
        input = remove_dupes(ListNode.build([0, 11, 11, 22, 33]))
        output = ListNode.build([0, 11, 22, 33])
        self.assertEqual(input, output)

    def test_1234567888(self):
        input = remove_dupes(ListNode.build([1, 2, 3, 4, 5, 6, 7, 8, 8, 8]))
        output = ListNode.build([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(input, output)

    def test_blank(self):
        input = remove_dupes(ListNode.build([]))
        output = ListNode.build([])
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
