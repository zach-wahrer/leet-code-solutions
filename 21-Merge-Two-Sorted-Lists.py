'''
Psudocode:
        Import values from both LinkedLists to a single list
        Sort them
        Build output linked list
'''

import unittest
from models.linkedList import ListNode


def merge_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:

    def to_list(head: ListNode) -> list:
        output = list()
        while head:
            output.append(head.val)
            head = head.next
        return output

    def to_linked_list(values: list) -> ListNode:
        head = ListNode(values[0])
        current_node = head
        for i in values[1:]:
            current_node.next = ListNode(i)
            current_node = current_node.next
        return head

    linked_list_values = list()
    for i in to_list(l1) + to_list(l2):
        linked_list_values.append(i)
    linked_list_values.sort()
    return to_linked_list(linked_list_values)


class TestListMerge(unittest.TestCase):

    def test_124_134(self):
        list1 = ListNode.build([1, 2, 4])
        list2 = ListNode.build([1, 3, 4])
        input = merge_sorted_lists(list1, list2)
        output = ListNode.build([1, 1, 2, 3, 4, 4])
        self.assertEqual(input, output)

    def test_81632_519100(self):
        list1 = ListNode.build([8, 16, 32])
        list2 = ListNode.build([5, 19, 100])
        input = merge_sorted_lists(list1, list2)
        output = ListNode.build([5, 8, 16, 19, 32, 100])
        self.assertEqual(input, output)

    def test_minus1248_minus6945(self):
        list1 = ListNode.build([-12, 4, 8])
        list2 = ListNode.build([-6, 9, 45])
        input = merge_sorted_lists(list1, list2)
        output = ListNode.build([-12, -6, 4, 8, 9, 45])
        self.assertEqual(input, output)

    def test_uneven_lists(self):
        list1 = ListNode.build([1, 2, 3, 4])
        list2 = ListNode.build([-99, 4, 32])
        input = merge_sorted_lists(list1, list2)
        output = ListNode.build([-99, 1, 2, 3, 4, 4, 32])
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
