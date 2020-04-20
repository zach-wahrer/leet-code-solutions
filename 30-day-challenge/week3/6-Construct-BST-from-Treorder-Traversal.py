import unittest
from binaryTree import TreeNode


# Recursive solution
def build_bst(preorder: list) -> TreeNode:
    if not preorder:
        return TreeNode("")

    head = TreeNode(preorder[0])

    def _add(value, node):
        if value < node.val:
            if not node.left:
                node.left = TreeNode(value)
            else:
                _add(value, node.left)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                _add(value, node.right)

    for value in preorder[1:]:
        _add(value, head)

    return head


class TestBSTBuild(unittest.TestCase):
    def test_85171012(self):
        test_head = TreeNode()
        test_head.build_from_heap([8, 5, 10, 1, 7, None, 12])
        self.assertEqual(build_bst([8, 5, 1, 7, 10, 12]), test_head)


if __name__ == "__main__":
    unittest.main()
