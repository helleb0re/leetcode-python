from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    buffer = deque([root])
    while buffer:
        curr = buffer.popleft()
        curr.left, curr.right = curr.right, curr.left

        if curr.left:
            buffer.append(curr.left)

        if curr.right:
            buffer.append(curr.right)

    return root


# dfs, iterative
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    buffer = [root]
    while buffer:
        curr = buffer.pop()

        if curr.right:
            buffer.append(curr.right)

        if curr.left:
            buffer.append(curr.left)

        curr.left, curr.right = curr.right, curr.left

    return root


# dfs, recursive
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root


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
        buffer.extend(tmp_buffer)


if __name__ == "__main__":
    root = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    invertTree(root)
    printTree(root)
