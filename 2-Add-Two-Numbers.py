'''
Psudocode:
    For each list:
        Traverse list, building number
        Reverse values
    Add two numbers
    Reverse values,
    Build linked list and return head node
'''

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


def add_linked_lists(l1: ListNode, l2: ListNode) -> ListNode:
    head_nodes = [l1, l2]
    out_numbers = ["", ""]
    for i, head in enumerate(head_nodes):
        out_numbers[i] = get_list_number(head)
    return out_numbers[0] + out_numbers[1]


def get_list_number(head: ListNode) -> int:
    number = list()
    while head:
        number.append(head.val)
        head = head.next
    number.reverse()
    return int(''.join(map(str, number)))


class TestAddingLinkedLists(unittest.TestCase):

    def test_342_465(self):
        lists = [[2, 4, 3], [5, 6, 4]]
        head = list()
        for i, numbers in enumerate(lists):
            head.append(ListNode(numbers[0]))
            for digit in numbers[1:]:
                head[i].add(digit)
        input = add_linked_lists(head[0], head[1])
        output = 807
        self.assertEqual(input, output)

    def test_4580_88900(self):
        lists = [[0, 8, 5, 4], [0, 0, 9, 8, 8]]
        head = list()
        for i, numbers in enumerate(lists):
            head.append(ListNode(numbers[0]))
            for digit in numbers[1:]:
                head[i].add(digit)
        input = add_linked_lists(head[0], head[1])
        output = 93480
        self.assertEqual(input, output)

    def test_neg_101_101(self):
        lists = [[1, 0, -1], [1, 0, 1]]
        head = list()
        for i, numbers in enumerate(lists):
            head.append(ListNode(numbers[0]))
            for digit in numbers[1:]:
                head[i].add(digit)
        input = add_linked_lists(head[0], head[1])
        output = 0
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
