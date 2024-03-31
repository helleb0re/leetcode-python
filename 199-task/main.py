from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) BFS solution
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    buffer = [root]
    res = []

    while buffer:

        new_buffer = []
        for node in buffer:

            if node.left is not None:
                new_buffer.append(node.left)

            if node.right is not None:
                new_buffer.append(node.right)

        res.append(buffer[-1].val)

        buffer.clear()
        buffer = new_buffer

    return res


if __name__ == "__main__":
    root = TreeNode(
        1, TreeNode(2, None, TreeNode(5, TreeNode(4))), TreeNode(3, TreeNode(6))
    )
    assert rightSideView(root) == [1, 3, 6, 4]

    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert rightSideView(root) == [1, 3, 4]

    root = TreeNode(1, None, TreeNode(3))
    assert rightSideView(root) == [1, 3]

    root = None
    assert rightSideView(root) == []
