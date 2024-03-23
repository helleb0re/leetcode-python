from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs
def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    buffer = deque([root])

    depth = 0
    while buffer:

        tmp_buffer = []
        for curr in buffer:
            if curr.left is not None:
                tmp_buffer.append(curr.left)

            if curr.right is not None:
                tmp_buffer.append(curr.right)

        depth += 1
        buffer.clear()
        buffer.extend(tmp_buffer)

    return depth


# dfs, recursive
def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth_left = maxDepth(root.left)
    depth_right = maxDepth(root.right)
    depth = max(depth_left, depth_right) + 1

    return depth


# dfs, iterative
def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth = 1
    buffer = [(root, depth)]

    while buffer:

        curr, curr_depth = buffer.pop()

        if curr.right is not None:
            buffer.append((curr.right, curr_depth + 1))

        if curr.left is not None:
            buffer.append((curr.left, curr_depth + 1))

        depth = max(depth, curr_depth)

    return depth


def printTree(root):
    buffer = [root]

    while buffer:
        tmp_buffer = []
        for elem in buffer:
            print(elem.val, end=" ")

            if elem.left:
                tmp_buffer.append(elem.left)

            if elem.right:
                tmp_buffer.append(elem.right)
        print()

        buffer.clear()
        buffer += tmp_buffer


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert maxDepth(root) == 3
