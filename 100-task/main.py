from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs, recursive
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif (
        (p is None and q is not None)
        or (p is not None and q is None)
        or (p.val != q.val)
    ):
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# dfs, iterative
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    buffer = [(p, q)]
    while buffer:
        curr_p, curr_q = buffer.pop()

        if curr_p is None and curr_q is None:
            continue

        if (
            (curr_p is None and curr_q is not None)
            or (curr_p is not None and curr_q is None)
            or curr_p.val != curr_q.val
        ):
            return False

        buffer.append((curr_p.right, curr_q.right))
        buffer.append((curr_p.left, curr_q.left))

    return True


if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTree(root1, root2)

    root1 = TreeNode(1, TreeNode(2), TreeNode())
    root2 = TreeNode(1, TreeNode(), TreeNode(2))
    assert not isSameTree(root1, root2)

    root1 = TreeNode(1, TreeNode(1), TreeNode(2))
    root2 = TreeNode(1, TreeNode(2), TreeNode(1))
    assert not isSameTree(root1, root2)
