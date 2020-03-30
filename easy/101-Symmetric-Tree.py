import unittest
from models.binaryTree import TreeNode


def is_symmetric(root: TreeNode) -> bool:
    pass


class TestSymmetry(unittest.TestCase):

    def test_true(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(is_symmetric(root))

    def test_false(self):
        root = TreeNode()
        root.build_from_heap([1, 2, 2, None, 3, None, 3])
        self.assertTrue(is_symmetric(root))


if __name__ == "__main__":
    unittest.main()
