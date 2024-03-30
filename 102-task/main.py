from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my O(n) BFS solution
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    buffer = [root]
    res = []

    while buffer:

        level_nodes = []
        next_level_nodes = []

        for curr_node in buffer:
            level_nodes.append(curr_node.val)

            if curr_node.left:
                next_level_nodes.append(curr_node.left)

            if curr_node.right:
                next_level_nodes.append(curr_node.right)

        res.append(level_nodes)

        buffer.clear()
        buffer = next_level_nodes

    return res


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert levelOrder(root) == [[3], [9, 20], [15, 7]]

    root = TreeNode(1)
    assert levelOrder(root) == [[1]]

    root = None
    assert levelOrder(root) == []
