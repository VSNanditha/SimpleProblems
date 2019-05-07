# A binary tree is a tree which is characterized by one of the following properties:
#
# * It can be empty (null).
# * It contains a root node only.
# * It contains a root node with a left subtree, a right subtree, or both. These subtrees are also binary trees.
#
# In-order traversal is performed as
#
# 1. Traverse the left subtree.
# 2. Visit root.
# 3. Traverse the right subtree.
#
# For this in-order traversal, start from the left child of the root node and keep exploring the left subtree until
# you reach a leaf. When you reach a leaf, back up to its parent, check for a right child and visit it if there is one.
# If there is not a child, you've explored its left and right subtrees fully. If there is a right child, traverse its
# left subtree then its right in the same manner. Keep doing this until you have traversed the entire tree. You will
# only store the values of a node as you visit when one of the following is true:
#
# * it is the first node visited, the first time visited
# * it is a leaf, should only be visited once
# * all of its subtrees have been explored, should only be visited once while this is true
# * it is the root of the tree, the first time visited
#
# Swapping: Swapping subtrees of a node means that if initially node has left subtree L and right subtree R, then after
# swapping, the left subtree will be R and the right subtree, L.
#
# For example, in the following tree, we swap children of node 1.
#
#                                 Depth
#     1               1            [1]
#    / \             / \
#   2   3     ->    3   2          [2]
#    \   \           \   \
#     4   5           5   4        [3]
#
# In-order traversal of left tree is 2 4 1 3 5 and of right tree is 3 5 1 2 4.
#
# Swap operation:
#
# We define depth of a node as follows:
#
# * The root node is at depth 1.
# * If the depth of the parent node is d, then the depth of current node will be d+1.
#
# Given a tree and an integer, k, in one operation, we need to swap the subtrees of all the nodes at each depth h,
# where h ∈ [k, 2k, 3k,...]. In other words, if h is a multiple of k, swap the left and right subtrees of that level.
#
# You are given a tree of n nodes where nodes are indexed from [1..n] and it is rooted at 1. You have to perform t swap
# operations on it, and after each swap operation print the in-order traversal of the current state of the tree.
#
# Function Description
#
# Complete the swapNodes function in the editor below. It should return a two-dimensional array where each element is
# an array of integers representing the node indices of an in-order traversal after a swap operation.
#
# swapNodes has the following parameter(s):
# - indexes: an array of integers representing index values of each node[i], beginning with node[1], the first element,
#   as the root.
# - queries: an array of integers, each representing a k value.
#
# Input Format
# The first line contains n, number of nodes in the tree.
#
# Each of the next n lines contains two integers, a b, where a is the index of left child, and b is the index of right
# child of ith node.
#
# Note: -1 is used to represent a null node.
#
# The next line contains an integer, t, the size of queries.
# Each of the next t lines contains an integer queries[i], each being a value k.
#
# Output Format
# For each k, perform the swap operation and store the indices of your in-order traversal to your result array.
# After all swap operations have been performed, return your result array for printing.
#
# Constraints
#
# * 1 <= n <= 1024
# * 1 <= t <= 100
# * 1 <= k <= n
# * Either a = -1 or 2 <= a <= n
# * Either b = -1 or 2 <= b <= n
# * The index of a non-null child will always be greater than that of its parent.
from queue import Queue
import sys



class TreeNode:
    def __init__(self, value, height):
        self.data = value
        self.left = None
        self.right = None
        self.height = height

    def build_tree(self, indexes):
        """
        :param indexes:
        :return:
        """
        root = self
        queue = Queue()
        queue.put(root)
        for i in range(len(indexes)):
            current = queue.get()
            # print(current.data)
            current.left = TreeNode(indexes[i][0], current.height + 1) if indexes[i][0] != -1 \
                else None
            current.right = TreeNode(indexes[i][1], current.height + 1) if indexes[i][1] != -1\
                else None
            if current.left is not None:
                queue.put(current.left)
            if current.right is not None:
                queue.put(current.right)

    def print_tree(self, tree):
        """
        Prints In-Order traversal of the tree
        """
        if self is None:
            return
        if self.left:
            self.left.print_tree(tree)
        # print(self.data, end=' ')
        tree.append(self.data)
        if self.right:
            self.right.print_tree(tree)
        return tree

    # def identify_depths(self):
    #     node_depths = [[] for _ in range(1024)]
    #     if self is None:
    #         return
    #     node_depths[1] = [self]
    #     queue = Queue()
    #     queue.put(self)
    #     while not(queue.empty()):
    #         current = queue.get()
    #         height = current.height
    #         if current.left is not None:
    #             node_depths[height+1].append(current.left)
    #             queue.put(current.left)
    #         if current.right is not None:
    #             node_depths[height+1].append(current.right)
    #             queue.put(current.right)
    #     return node_depths


def swap_nodes(indexes, queries):
    """
    :param indexes:
    :param queries:
    :return:
    """
    tree = TreeNode(1, 1)
    tree.build_tree(indexes)
    # print('tree initial:', tree.print_tree([]))
    queue = Queue()
    result = []
    for query in queries:
        # print('query:', query)
        queue.put(tree)
        while not (queue.empty()):
            query_list =  [query * x for x in range(1, max(queries)+1)]
            current = queue.get()
            # print('entering while', current, current.data, current.left, current.right, current.height)
            if current.left is not None:
                queue.put(current.left)
            if current.right is not None:
                queue.put(current.right)
            if current.left is not None and current.right is not None and current.height in query_list:
                # print('swapping ', current.left.data, 'and', current.right.data)
                temp = current.left
                current.left = current.right
                current.right = temp
            elif current.left is not None and current.right is None and current.height in query_list:
                # print('swapping ', current.left.data, 'and None')
                current.right = current.left
                current.left = None
            elif current.left is None and current.right is not None and current.height in query_list:
                # print('swapping ', 'c    mNone and', current.right.data)
                current.left = current.right
                current.right = None
        result.append(tree.print_tree([]))
    return result


if __name__ == '__main__':
    sys.setrecursionlimit(100)
    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swap_nodes(indexes, queries)
    print('\n'.join([' '.join(map(str, x)) for x in result]))
