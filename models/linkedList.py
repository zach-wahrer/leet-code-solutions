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

    def __iter__(self):
        current = self
        while current is not None:
            yield current.val
            current = current.next

    # def __next__(self):
    #     if self.next is not None:
    #         value = self.val
    #         self = self.next
    #         return value
    #     raise StopIteration

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

    def build_circular(values: list):
        head = ListNode.build(values)
        first_node = head
        while head:
            if head.next is None:
                head.next = first_node
                return first_node
            head = head.next

    def length(self) -> int:
        return len(self.to_list())

    def is_circular(self) -> bool:
        move_one = self
        if self.next is None:  # Check for single node
            return False
        move_two = self.next.next
        while True:
            if not move_one or not move_two:
                return False
            elif move_one == move_two:
                return True
            else:
                move_one = move_one.next
                # Don't run off the end of odd numbered, non-circular lists
                if not move_two.next:
                    return False
                move_two = move_two.next.next

    def to_list(self) -> list:
        values = list()
        head = self
        if head.is_circular():
            return False
        while head:
            values.append(head.val)
            head = head.next
        return values

    def to_set(self) -> set:
        return set(self.to_list())
