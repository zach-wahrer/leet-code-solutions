import unittest
from models.binary_tree import TreeNode


def convert_array(nums: list) -> TreeNode:
    pass


class TestBinarySearchTree(unittest.TestCase):

    def test_5_digits(self):
        built_tree = convert_array([-10, -3, 0, 5, 9])
        test_tree = TreeNode()
        test_tree.build_from_heap([0, -3, 9, -10, None, 5])
        self.assertEqual(built_tree, test_tree)


if __name__ == "__main__":
    unittest.main()
