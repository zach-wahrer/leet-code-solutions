# Linked List

import unittest


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def add(self, new_val):
        if self.val is None:
            self.val = new_val
        elif self.next is None:
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
        if values:
            head = ListNode(values[0])
            for value in values[1:]:
                head.add(value)
        else:
            head = ListNode(None)
        return head

    def length(self) -> int:
        return len(self.to_list())

    def check_for_circular(self) -> bool:
        move_one = self
        move_two = self.next.next
        while True:
            if not move_one or not move_two:
                return False
            elif move_one == move_two:
                return True
            else:
                move_one = move_one.next
                move_two = move_two.next.next

    def to_list(self) -> list:
        values = list()
        head = self
        while head:
            values.append(head.val)
            head = head.next
        return values

    def to_set(self) -> set:
        return set(self.to_list())
