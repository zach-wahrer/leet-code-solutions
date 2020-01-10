import unittest
from linkedList import ListNode


class TestLinkedList(unittest.TestCase):

    def test_123(self):
        input = [1, 2, 3]
        linked_list = ListNode.build(input)
        output = linked_list.to_list()
        self.assertEqual(input, output)

    def test_minus8634(self):
        input = [-8, -9, -3, -4]
        linked_list = ListNode.build(input)
        output = linked_list.to_list()
        self.assertEqual(input, output)

    def test_string(self):
        input = ['this', 'is', 'a', 'string', 'test']
        linked_list = ListNode.build(input)
        output = linked_list.to_list()
        self.assertEqual(input, output)

    def test_large(self):
        input = [2**30, -30**5, 8**16, 100*1000000]
        linked_list = ListNode.build(input)
        output = linked_list.to_list()
        self.assertEqual(input, output)


if __name__ == "__main__":
    unittest.main()
