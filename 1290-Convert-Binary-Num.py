# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Psudocode:
    FOR SINGLY-LINKED LIST TRAVERSAL
    Go to first ListNode
    Append ListNode.value to binary number list
    Go to second ListNode
    Append ListNode.value to binary number list
    Repeat until ListNode.next = None

    FOR BINARY CONVERSION
    Reverse the list.
    Loop through list.
        If the digit is a 1
            Add the value of the current place to the final number
            If the place value is one
                Only increment by one
        Else
            If the place value is one
                Only increment by one
            Else
                Double the place value
    Return final number
"""


import unittest


def convert_binary(head: list) -> int:
    binary_number = traverse_list(head)
    return int(binary_number, 2)


def traverse_list(head: list) -> str:
    binary_number = str()
    while True:
        binary_number += str(head.val)
        if head.next is None:
            break
        else:
            head = head.next
    return binary_number


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


class TestBin(unittest.TestCase):

    def test_101(self):
        binary_number = [1, 0, 1]
        head = ListNode(binary_number[0])
        for digit in binary_number[1:]:
            head.add(digit)
        input = convert_binary(head)
        output = 5
        self.assertEqual(input, output)

    def test_0(self):
        binary_number = [0]
        head = ListNode(binary_number[0])
        input = convert_binary(head)
        output = 0
        self.assertEqual(input, output)

    def test_00(self):
        binary_number = [0, 0]
        head = ListNode(binary_number[0])
        for digit in binary_number[1:]:
            head.add(digit)
        input = convert_binary(head)
        output = 0
        self.assertEqual(input, output)

    def test_01101(self):
        binary_number = [0, 1, 1, 0, 1]
        head = ListNode(binary_number[0])
        for digit in binary_number[1:]:
            head.add(digit)
        input = convert_binary(head)
        output = 13
        self.assertEqual(input, output)

    def test_11011(self):
        binary_number = [1, 1, 0, 1, 1]
        head = ListNode(binary_number[0])
        for digit in binary_number[1:]:
            head.add(digit)
        input = convert_binary(head)
        output = 27
        self.assertEqual(input, output)

    def test_10010001(self):
        binary_number = [1, 0, 0, 1, 0, 0, 0, 1]
        head = ListNode(binary_number[0])
        for digit in binary_number[1:]:
            head.add(digit)
        input = convert_binary(head)
        output = 145
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
    # convert_binary([1, 0, 1])
