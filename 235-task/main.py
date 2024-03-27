# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    while True:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root


if __name__ == "__main__":
    root = TreeNode(
        6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)),
    )
    assert lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val == 6

    root = TreeNode(
        6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)),
    )
    assert lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val == 2

    root = TreeNode(
        2,
        TreeNode(1),
    )
    assert lowestCommonAncestor(root, TreeNode(2), TreeNode(1)).val == 2
