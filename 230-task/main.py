from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my recursive dfs O(n) solution
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    answer = -1

    def dfs(node):
        if node is None:
            return

        dfs(node.left)

        nonlocal k
        k -= 1
        if k == 0:
            nonlocal answer
            answer = node.val

        dfs(node.right)

    dfs(root)
    return answer


# my iterative bfs O(n) solution with arr.len == n
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    buffer = [(root, 0)]

    arr = []
    while buffer:
        curr_node, ind = buffer.pop()

        if curr_node.left:
            buffer.append((curr_node.left, ind))

        if curr_node.right:
            buffer.append((curr_node.right, ind + 1))

        arr.insert(ind, curr_node.val)

    return arr[k - 1]


# my iterative dfs O(n) solution
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    curr_node = root
    stack = []

    while curr_node:
        if curr_node.left:
            stack.append(curr_node)
            curr_node = curr_node.left
            continue

        k -= 1
        if k == 0:
            return curr_node.val
        # print(curr_node.val)

        if curr_node.right:
            curr_node = curr_node.right
            continue

        if not stack:
            break

        curr_node = stack.pop()
        curr_node.left = None

    return -1


# neetcode iterative dfs O(n) solution
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    curr_node = root
    stack = []

    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left

        curr_node = stack.pop()
        k -= 1
        if k == 0:
            return curr_node.val
        # print(curr_node.val)
        curr_node = curr_node.right

    return -1


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    assert kthSmallest(root, 3) == 3

    root = TreeNode(
        10, TreeNode(3, None, TreeNode(7, TreeNode(5), TreeNode(8))), TreeNode(12)
    )
    assert kthSmallest(root, 3) == 7
