from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(root: Optional[TreeNode]):
        if root is None:
            return 0

        depth_left = dfs(root.left)
        depth_right = dfs(root.right)

        nonlocal res
        res = max(res, depth_left + depth_right)

        return max(depth_left, depth_right) + 1

    dfs(root)

    return res


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameterOfBinaryTree(root) == 3
