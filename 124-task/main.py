from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my first solution
def maxPathSum(root: Optional[TreeNode]) -> int:
    best_answer = -1001

    def dfs(node):
        if node is None:
            return -1001

        left_res = dfs(node.left)
        right_res = dfs(node.right)

        nonlocal best_answer
        best_answer = max(
            best_answer,
            max(
                max(max(left_res, right_res), node.val + left_res + right_res), node.val
            ),
        )

        return max(max(left_res, right_res) + node.val, node.val)

    last_res = dfs(root)
    best_answer = max(best_answer, last_res)
    return best_answer


# my improved solution
def maxPathSum(root: Optional[TreeNode]) -> int:
    best_answer = float("-inf")

    def dfs(node):
        if node is None:
            return 0

        left_res = dfs(node.left)
        right_res = dfs(node.right)

        nonlocal best_answer
        best_answer = max(
            best_answer,
            node.val + left_res + right_res,
        )

        return max(max(left_res, right_res) + node.val, 0)

    dfs(root)
    return best_answer


# neetcode solution
def maxPathSum(root: Optional[TreeNode]) -> int:
    best_answer = float("-inf")

    def dfs(node):
        if node is None:
            return 0

        left_res = dfs(node.left)
        left_res = max(left_res, 0)
        right_res = dfs(node.right)
        right_res = max(right_res, 0)

        nonlocal best_answer
        best_answer = max(
            best_answer,
            node.val + left_res + right_res,
        )

        return max(left_res, right_res) + node.val

    dfs(root)
    return best_answer


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert maxPathSum(root) == 6

    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert maxPathSum(root) == 42

    root = TreeNode(-2, TreeNode(1))
    assert maxPathSum(root) == 1

    root = TreeNode(-2)
    assert maxPathSum(root) == -2

    root = TreeNode(
        1,
        TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)),
        TreeNode(-3, TreeNode(-2), None),
    )
    assert maxPathSum(root) == 3

    root = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
    )
    assert maxPathSum(root) == 48
