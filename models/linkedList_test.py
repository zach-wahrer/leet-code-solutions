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

    def test_longer_equality(self):
        input = [1, 2, 'b', 8, 'xyz', 3.14]
        linked_list = ListNode.build(input)
        linked_list2 = ListNode.build(input)
        self.assertEqual(linked_list, linked_list2)

    def test_longer_inequality(self):
        input = [1, 2, 'b', 8, 'xyz', 3.14]
        linked_list = ListNode.build(input)
        linked_list2 = ListNode.build(input[0:1])
        self.assertNotEqual(linked_list, linked_list2)

    def test_empty_input_array(self):
        linked_list = ListNode.build([])
        output = ListNode(None)
        self.assertEqual(linked_list, output)

    def test_empty_input_array_with_non_empty(self):
        linked_list = ListNode.build([1, 2, 3])
        output = ListNode(None)
        self.assertNotEqual(linked_list, output)

    def test_add_to_empty_ListNode_replaces_empty_node(self):
        nil_node = ListNode(None)
        nil_node.add(5)
        self.assertEqual(nil_node.val, 5)
        self.assertEqual(nil_node.next, None)


class TestLinkedListHelpers(unittest.TestCase):

    def test_to_set(self):
        input = [1, 'a', 2, 'x', 'x']
        linked_list = ListNode.build(input)
        output = linked_list.to_set()
        self.assertEqual({1, 'a', 2, 'x'}, output)

    def test_length(self):
        input = [1, 1000, 8, 9, 'abba']
        linked_list = ListNode.build(input)
        output = linked_list.length()
        self.assertEqual(5, output)

    def test_all_unique_false(self):
        input = [5, 6, 7, 8, 'z', 8]
        linked_list = ListNode.build(input)
        self.assertFalse(linked_list.all_unique())

    def test_all_unique_true(self):
        input = ['a', 'b', 'c', 'aa', 11, 1]
        linked_list = ListNode.build(input)
        self.assertTrue(linked_list.all_unique())


if __name__ == "__main__":
    unittest.main()
