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


def build_binary(head):
    pointer = head
    binary = list()

    while True:
        binary.append(pointer.val)
        if pointer.next is None:
            break
        else:
            pointer = pointer.next


def convert_binary(binary):
    number = 0
    value = 1
    binary.reverse()
    for i in binary:
        if i == 1:
            number += value
            if value == 1:
                value += 1
            else:
                value *= 2
        else:
            if value == 1:
                value += 1
            else:
                value *= 2
    return number


class TestBin(unittest.TestCase):

    def test_101(self):
        input = convert_binary([1, 0, 1])
        output = 5
        self.assertEqual(input, output)

    def test_0(self):
        input = convert_binary([0])
        output = 0
        self.assertEqual(input, output)

    def test_00(self):
        input = convert_binary([0, 0])
        output = 0
        self.assertEqual(input, output)

    def test_01101(self):
        input = convert_binary([0, 1, 1, 0, 1])
        output = 13
        self.assertEqual(input, output)

    def test_11011(self):
        input = convert_binary([1, 1, 0, 1, 1])
        output = 27
        self.assertEqual(input, output)

    def test_10010001(self):
        input = convert_binary([1, 0, 0, 1, 0, 0, 0, 1])
        output = 145
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
    # convert_binary([1, 0, 1])
