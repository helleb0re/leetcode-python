from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my approach: O(n1) iterative dfs solution
# n1: amount of root's node
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    buffer_root = [root]
    buffer_subRoot = [subRoot]

    def isSameNode(node1, node2):
        if (
            node1.val == node2.val
            and (node1.left and node2.left or not node1.left and not node2.left)
            and (node1.right and node2.right or not node1.right and not node2.right)
        ):
            return True

        return False

    while buffer_root:
        curr_root_node = buffer_root.pop()
        curr_subRoot_node = buffer_subRoot.pop()

        if isSameNode(curr_root_node, curr_subRoot_node):
            if curr_subRoot_node.right is not None:
                buffer_subRoot.append(curr_subRoot_node.right)

            if curr_subRoot_node.left is not None:
                buffer_subRoot.append(curr_subRoot_node.left)
        else:
            buffer_subRoot.clear()

            if isSameNode(curr_root_node, subRoot):
                if subRoot.right is not None:
                    buffer_subRoot.append(subRoot.right)

                if subRoot.left is not None:
                    buffer_subRoot.append(subRoot.left)
            else:
                buffer_subRoot.append(subRoot)

        if len(buffer_subRoot) == 0:
            return True

        if curr_root_node.right is not None:
            buffer_root.append(curr_root_node.right)

        if curr_root_node.left is not None:
            buffer_root.append(curr_root_node.left)

    return False


# neetcode approach: O(n1 * n2) recursive dfs solution
# n1: amount of root's node
# n2: amount of subRoot's node
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if subRoot is None:
        return True
    if root is None:
        return False

    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None and q is not None or p is not None and q is None:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    assert isSubtree(root, subRoot)

    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    assert not isSubtree(root, subRoot)

    root = TreeNode(
        1,
        None,
        TreeNode(
            1,
            None,
            TreeNode(1, None, TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(2)))),
        ),
    )
    subRoot = TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(2)))
    assert isSubtree(root, subRoot)
