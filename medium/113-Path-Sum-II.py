import unittest
from models.binary_tree import TreeNode


def path_sum(root: TreeNode, sum: int) -> list:
    pass


class TestPathSum(unittest.TestCase):

    def test_two_paths_22(self):
        tree = TreeNode()
        tree.build_from_heap([5, 4, 8, 11, None, 13, 4, 7, 2,
                              None, None, None, None, 5, 1])
        self.assertEqual(path_sum(tree, 22), [[5, 4, 11, 2], [5, 8, 4, 5]])


if __name__ == "__main__":
    unittest.main()
