class TreeNode:
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None

    def build_from_heap(self, input_list):
        input_list.insert(0, 0)
        for index, data in enumerate(input_list):
            if data is not None:
                if index == 1 or index == 0:
                    self.val = data
                    continue

                current_level = 2

                self.add(data, current_level, index)

    def add(self, data, current_level, index):
        if index in list(range(1, current_level * 2)):
            if index % 2 == 0:
                self.left = TreeNode(data)
            else:
                self.right = TreeNode(data)
        else:
            side = index // current_level
            if side % 2 == 0:
                self.left.add(data, current_level * 2, index)

            else:
                self.right.add(data, current_level * 2, index)


def preorder(tree, depth=0):
    if tree:
        print(tree.val, depth)
        if tree.left:
            print("Lower left: ", tree.left.val)
        if tree.right:
            print("Lower right: ", tree.right.val)
        depth += 1
        preorder(tree.left, depth)
        preorder(tree.right, depth)
