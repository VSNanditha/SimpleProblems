# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node
# in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.
import math


class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data < data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.add_child(data)
        elif self.data > data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.add_child(data)
        else:
            self.data = data

    def print_tree(self):
        if self is None:
            return
        print(self.data, sep='\s')
        if self.left:
            print('left', self.left.data)
            self.left.print_tree()
        if self.right:
            print('right', self.right.data)
            self.right.print_tree()


def max_path_sum(root, result):
    """
    :param root: root node
    :param result: max sum till parsed node
    :return:
    """
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    ls = max_path_sum(root.left, result)
    rs = max_path_sum(root.right, result)
    result[0] = max(result[0], ls + rs + root.data)
    if root.left is not None and root.right is not None:
        return max(ls, rs) + root.data
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data


if __name__ == '__main__':
    tree = list(map(int, input("Enter tree node values with space separation").rstrip().split()))
    root = TreeNode(tree[0])
    for node in tree:
        root.add_child(node)
    root.print_tree()
    result = [-math.inf]
    max_path_sum(root, result)
    print('Max Path Sum of the Tree is ', result[0])
