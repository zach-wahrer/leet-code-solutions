# Linked List

import unittest


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, new_val):
        if self.next is None:
            self.next = ListNode(new_val)
        else:
            self.next.add(new_val)
        return self

    def add_itter(self, new_val):
        """Reduntant add function"""
        current_node = self
        while current_node.next:
            current_node = self.next
        current.next = ListNode(new_val)
