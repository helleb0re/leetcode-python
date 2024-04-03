from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my recursive dfs solution
# version 1
def isValidBST(root: Optional[TreeNode]) -> bool:
    last_elem = float("-inf")
    answer = True

    def dfs(node):
        if node is None:
            return

        dfs(node.left)

        nonlocal last_elem
        if last_elem >= node.val:
            nonlocal answer
            answer = False

        last_elem = node.val

        dfs(node.right)

    dfs(root)
    return answer


# my recursive dfs solution
# version 2
def isValidBST(root: Optional[TreeNode]) -> bool:

    def dfs(node, ans, last_elem):
        if node is None:
            return ans, last_elem

        ans, last_elem = dfs(node.left, ans, last_elem)

        if last_elem >= node.val:
            ans = False

        last_elem = node.val

        ans, last_elem = dfs(node.right, ans, last_elem)

        return ans, last_elem

    return dfs(root, True, float("-inf"))[0]


# neetcode recursive dfs solution
def isValidBST(root: Optional[TreeNode]) -> bool:

    def dfs(node, left_val, right_val):
        if node is None:
            return True
        elif node.val < left_val or node.val > right_val:
            return False

        return dfs(node.left, left_val, node.val) and dfs(
            node.right, node.val, right_val
        )

    return dfs(root, float("-inf"), float("inf"))


# my iterative dfs solution
def isValidBST(root: Optional[TreeNode]) -> bool:
    buffer = [(root, float("-inf"), float("inf"))]

    while buffer:
        curr_node, left_val, right_val = buffer.pop()

        if not (left_val < curr_node.val < right_val):
            return False

        if curr_node.right:
            buffer.append((curr_node.right, curr_node.val, right_val))

        if curr_node.left:
            buffer.append((curr_node.left, left_val, curr_node.val))

    return True


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert isValidBST(root)

    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert not isValidBST(root)
