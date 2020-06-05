import unittest
from models.linkedList import ListNode


# O(n) solution - TOO MESSY, doesn't pass all tests
# Iterate through linked list with fast and slow pointer
# Fast reads the value 1 ahead to see if it == val
# If so, slow.next = slow.next.next to remove the value from list
# Return original head node
# Edge cases: Empty list, list one node long, first node removal, last node removal
def remove_linked_list_val_messy(head: ListNode, val: int) -> ListNode:
    if not head.next:  # Len = 1 or empty list edge case
        if head.val != val:
            return head
        else:
            return ListNode(None)

    while head.val == val:  # First list node to be removed edge case
        if head.next:
            head = head.next

        else:
            return ListNode(None)

    slow = head
    fast = head.next

    while fast.next:
        print(slow.val, fast.val)
        if fast.val == val:
            slow.next = slow.next.next
            slow = slow.next
            fast = fast.next.next
        else:
            slow = slow.next
            fast = fast.next

        if not fast.next:
            if fast.val == val:
                slow.next = None
            break
    if fast.val == val:  # Two item list with last val match edge case
        slow.next = None

    print(head.to_list())
    return head


# O(n) time, O(1) space solution
# Edge cases: Empty list, list one node long, first node removal, last node removal
def remove_linked_list_val(head: ListNode, val: int) -> ListNode:
    if head is None:
        return head

    start = head
    previous = None

    while start:

        if start.val == val:
            if previous is None:  # Start of list
                head = head.next
                start = head
            else:
                if not start.next:  # End of list
                    previous.next = None
                    break
                else:
                    start = start.next
                    previous.next = start
        else:
            previous = start
            start = start.next
        print(previous.val, start.val)

    if not head:
        return ListNode(None)

    return head


class TestRemovedLinkedList(unittest.TestCase):
    def test_1263456_6(self):
        input = remove_linked_list_val(ListNode.build([1, 2, 6, 3, 4, 5, 6]), 6)
        self.assertEqual(input, ListNode.build([1, 2, 3, 4, 5]))

    # def test_1578092_0(self):
    #     input = remove_linked_list_val(ListNode.build([-1, 5, 7, 0, 9, 2]), 0)
    #     self.assertEqual(input, ListNode.build([-1, 5, 7, 9, 2]))
    #
    # def test_9_9(self):
    #     input = remove_linked_list_val(ListNode.build([9]), 9)
    #     self.assertEqual(input, ListNode.build([None]))
    #
    # def test_9_1(self):
    #     input = remove_linked_list_val(ListNode.build([9]), 1)
    #     self.assertEqual(input, ListNode.build([9]))
    #
    # def test_blank(self):
    #     input = remove_linked_list_val(ListNode.build([]), None)
    #     self.assertEqual(input, ListNode.build([None]))
    #
    # def test_12_1(self):
    #     input = remove_linked_list_val(ListNode.build([1, 2]), 1)
    #     self.assertEqual(input, ListNode.build([2]))
    #
    # def test_12_2(self):
    #     input = remove_linked_list_val(ListNode.build([1, 2]), 2)
    #     self.assertEqual(input, ListNode.build([1]))
    #
    # def test_1122_1(self):
    #     input = remove_linked_list_val(ListNode.build([1, 1, 2, 2]), 1)
    #     self.assertEqual(input, ListNode.build([2, 2]))
    #
    # def test_1122_2(self):
    #     input = remove_linked_list_val(ListNode.build([1, 1, 2, 2]), 2)
    #     self.assertEqual(input, ListNode.build([1, 1]))
    #
    # def test_0000_0(self):
    #     input = remove_linked_list_val(ListNode.build([0, 0, 0, 0]), 0)
    #     self.assertEqual(input, ListNode.build([None]))


if __name__ == "__main__":
    unittest.main()
