from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The bottom up O(N) solution with dfs (recursive)
def isBalanced(root: Optional[TreeNode]) -> bool:
    answer = True

    def dfs(root: Optional[TreeNode]) -> None:
        if root is None:
            return 0

        depth_left = dfs(root.left)
        depth_right = dfs(root.right)

        if abs(depth_left - depth_right) > 1:
            nonlocal answer
            answer = False

        return max(depth_left, depth_right) + 1

    dfs(root)

    return answer


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert isBalanced(root)

    root = TreeNode(
        1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)
    )
    assert not isBalanced(root)
