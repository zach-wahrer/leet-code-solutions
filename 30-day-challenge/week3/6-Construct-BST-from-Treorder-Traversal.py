import unittest
from binaryTree import TreeNode


def build_bst(preorder: list) -> TreeNode:
    pass


class TestBSTBuild(unittest.TestCase):
    def test_85171012(self):
        test_head = TreeNode()
        test_head.build_from_heap([8, 5, 10, 1, 7, None, 12])
        self.assertEqual(build_bst([8, 5, 1, 7, 10, 12]), test_head)


if __name__ == "__main__":
    unittest.main()
