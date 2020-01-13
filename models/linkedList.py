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
        current_node.next = ListNode(new_val)

    def all_unique(self) -> bool:
        values = self.to_list()
        return len(values) == len(set(values))

    def build(values: list):
        head = ListNode(values[0])
        for value in values[1:]:
            head.add(value)
        return head

    def length(self) -> int:
        return len(self.to_list())

    def to_list(self) -> list:
        values = list()
        head = self
        while head:
            values.append(head.val)
            head = head.next
        return values

    def to_set(self) -> set:
        return set(self.to_list())
