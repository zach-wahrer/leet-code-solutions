import unittest

from models.linkedList import ListNode


def is_palindrome(head: ListNode) -> bool:
    node = head
    values = []

    while node:
        values.append(node.val)
        node = node.next

    i, j = 0, len(values) - 1
    while i < j:
        if values[i] != values[j]:
            return False
        i += 1
        j -= 1

    return True


class TestPalindromeLL(unittest.TestCase):
    def test_short_false(self):
        head = ListNode.build([1, 2])
        self.assertFalse(is_palindrome(head))

    def test_short_true(self):
        head = ListNode.build([1, 2, 2, 1])
        self.assertTrue(is_palindrome(head))


if __name__ == "__main__":
    unittest.main()
